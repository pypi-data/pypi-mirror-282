"""
GRPC server with simulated random bits for testing purposes
"""
from concurrent import futures
import logging
import threading
import grpc
import numpy as np
from . import uqrng_pb2, uqrng_pb2_grpc

DYNAMIC_RANGE = 2**14


def generate_random_numbers(n_bits: int):
    """
    Generates n 14 bit random numbers that are
    """
    rand_ints = np.random.randint(0, DYNAMIC_RANGE, size=n_bits)
    return "".join(format(num, "014b") for num in rand_ints)


class UqrngServer(uqrng_pb2_grpc.UqrngService):
    """
    Server class for simulate uqrng
    """

    def __init__(self):
        self.lock = threading.Lock()

    def GetQrns(self, request, context):
        """
        Generates random bit stream
        """
        if self.lock.acquire(blocking=False):
            bits_needed = request.n_bits
            while bits_needed > 0:
                # max number of qrns can take is 1000
                # on the client side this isn't important since can stream any amount
                qrn_bitstring = bytes(generate_random_numbers(n_bits=1000), "utf-8")
                if bits_needed < len(qrn_bitstring):
                    # take only the bits that are needed to complete request
                    qrn_bitstring = qrn_bitstring[:bits_needed]
                bits_needed -= len(qrn_bitstring)
                response = uqrng_pb2.RngOutput(qrn_bitstring=qrn_bitstring)
                yield response

            self.lock.release()
        else:
            context.set_code(grpc.StatusCode.UNAVAILABLE)
            context.set_details("Generator currently being accessed by another process")
            # required for to match function signature of output
            return uqrng_pb2.RngOutput()


class GrpcServer:
    """
    Provides basic functionality to start a threaded gRPC server instance

    :param ip_address: target ip address to start grpc server
    :param port: target port on which to start grpc server
    """

    def __init__(self, ip_address: str = "localhost", port: str = "50051"):
        self.stop_event = threading.Event()
        server_cls = UqrngServer()
        max_variables = 10000
        max_length = (
            int(
                ((((4 * max_variables**2)) + (4 * max_variables)) / (1024**2))
                + (
                    512
                    - (
                        (((4 * max_variables**2) + (4 * max_variables)) / (1024**2))
                        % 512
                    )
                )
            )
            * 1024**2
        )
        self.server = grpc.server(
            futures.ThreadPoolExecutor(max_workers=10),
            options=(
                ("grpc.max_receive_message_length", max_length),
                ("grpc.max_send_message_length", max_length),
            ),
        )

        uqrng_pb2_grpc.add_UqrngServiceServicer_to_server(server_cls, self.server)
        ip_address = ip_address if ip_address else "localhost"
        port = port if port else "50051"
        logging.info("grpc server ip_address:port %s:%s", ip_address, port)
        self.server.add_insecure_port(f"{ip_address}:{port}")

    def serve(self):
        """
        Starts grpc server instance which waits for termination
        """
        logging.info("Server started")
        self.server.start()
        self.server.wait_for_termination()

    def stop(self):
        """
        Stops the classes running grpc server instance
        with a stop event
        """
        self.server.stop(0)
        print("Stopping server")
        self.stop_event.set()
