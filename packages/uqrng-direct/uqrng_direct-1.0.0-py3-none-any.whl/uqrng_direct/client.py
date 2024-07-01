"""
Helper functions for interacting with QRNG through GRPC client
"""
from dataclasses import dataclass
from typing import List, Union
import time
import grpc

from .utils import message_to_dict, \
    SysStatus, \
    StatusDict, \
    resultNIST, \
    SystemInfoDict, \
    create_summary_table, \
    check_qrng_busy_error
  

from . import uqrng_pb2_grpc
from . import uqrng_pb2


@dataclass
class UqrngClient:
    """
    Client which provides access to QCI uqrng server interactions.

    :param ip_address: ip address of grpc server
    :param port: port of grpc server
    :param stub: the grpc stub that is created in the class
    :param channel: the grpc channel
    :note: stub used in all functions is a grpc server object
    """

    ip_address: str = "localhost"
    port: str = "50051"
    simulator: bool = False
    distribution: int = 2
    stub = None
    channel = None

    def __post_init__(self):
        max_data_size = 512 * 1024 * 1024
        ip_add_port = self.ip_address + ":" + self.port

        channel_opt = [
            ("grpc.max_send_message_length", max_data_size),
            ("grpc.max_receive_message_length", max_data_size),
        ]
        self.channel = grpc.insecure_channel(ip_add_port, options=channel_opt)
        self.stub = uqrng_pb2_grpc.UqrngServiceStub(self.channel)

    def GetEntropy(self, bits_of_entropy: int, wait: bool=False, timeout: int=0) -> bytes:
        """
        Streams random bits from uqrng device to client as bytes.

        :param bits_of_entropy: the number of bits to stream to the client
        :param wait: whether to wait for device to become available
        :param timeout: seconds to wait for QRNG device to become available. If is
            less than or equal to 0 than waits indefinitely.
        :return:  bitstring as bytes from the entropy source
        :note: Will return as :code:`UNAVAILABLE` with the following message when is in
            use 'QRNG currently in use'.
        """
        entropy_message = uqrng_pb2.RngInput(bits_of_entropy=bits_of_entropy)
        qrn_bytes = bytes()
        qrn_responses = self.stub.GetEntropy(
            entropy_message
        )
        try:
            for response in qrn_responses:
                qrn_bytes = qrn_bytes + response.entropy_bitstring
        except grpc.RpcError as err:
            if check_qrng_busy_error(rpc_err=err) and wait:
                print("QRNG in use waiting for access to device...")
               # countdown timeout before raising busy signal
                if timeout>0:
                    while (timeout>0):
                        time.sleep(1)
                        qrn_responses = self.stub.GetEntropy(
                            entropy_message
                        )
                        try:
                            for response in qrn_responses:
                                qrn_bytes = qrn_bytes + response.entropy_bitstring
                            # break out if able to get response
                            break
                        except grpc.RpcError as err:
                            timeout -= 1
                            if not check_qrng_busy_error(rpc_err=err):
                                raise
                            if timeout<=0:
                                raise
                # waits indefinitely to sample if device busy
                else:
                    while (True):
                        qrn_responses = self.stub.GetEntropy(
                            entropy_message
                        )
                        try:
                            for response in qrn_responses:
                                qrn_bytes = qrn_bytes + response.entropy_bitstring
                            # break out if able to get response
                            break
                        except grpc.RpcError as err:
                            if not check_qrng_busy_error(rpc_err=err):
                                raise
            else:
                raise
        return qrn_bytes

    def GetNoise(self, number_of_samples_requested: int, wait: bool=False, timeout: int=0) -> List[int]:
        """
        Random numbers from entropy source from device w/out post-processing.

        :param number_of_samples_requested: amount of random numbers requested
        :param wait: whether to wait for device to become available to sample
        :param timeout: seconds to wait for QRNG device to become available. If is
            less than or equal to 0 than waits indefinitely.

        :return: a list of integers in range 0-99,999
        :note: Will return as :code:`UNAVAILABLE` with the following message when is in
            use 'QRNG currently in use'.
        """
        noise_message = uqrng_pb2.NoiseInput(number_of_samples_requested=number_of_samples_requested)
        samples = []
        noise_responses = self.stub.GetNoise(
            noise_message
        )
        try:
            for response in noise_responses:
                samples += response.noise_source_data
        except grpc.RpcError as err:
            if check_qrng_busy_error(rpc_err=err) and wait:
                print("QRNG in use waiting for access to device...")
               # countdown timeout before raising busy signal
                if timeout>0:
                    while (timeout>0):
                        time.sleep(1)
                        noise_responses = self.stub.GetNoise(
                            noise_message
                        )
                        try:
                            for response in noise_responses:
                                samples += response.noise_source_data
                            # break out if able to get response
                            break
                        except grpc.RpcError as err:
                            timeout -= 1
                            if not check_qrng_busy_error(rpc_err=err):
                                raise
                            if timeout<=0:
                                raise
                                
                else:
                    # waits indefinitely if timeout less than 0
                    while (True):
                        noise_responses = self.stub.GetNoise(
                            noise_message
                        )
                        try:
                            for response in noise_responses:
                                samples += response.noise_source_data
                            # break out if able to get response
                            break
                        except grpc.RpcError as err:
                            if not check_qrng_busy_error(rpc_err=err):
                                raise
            else:
                raise
        return samples
        

    def HealthTest(self, wait: bool = True) -> Union[resultNIST, StatusDict]:
        """
        Runs all tests from National Institute of Standards and Technology (NIST) Statistical
        Test Suite for random and pseudo random numbers NIST SP 800-22 version 2.1.1.
        When run HealthTests are queued until the device becomes idle
        All tests are run with the default parameters. The NIST tests are run on 10 
        bitstreams of 1 million samples each. A full list of the tests that are as follows:

           - [01] Frequency
           - [02] Block Frequency
           - [03] Cumulative Sums
           - [04] Runs
           - [05] Longest Run of Ones
           - [06] Rank
           - [07] Discrete Fourier Transform
           - [08] Nonperiodic Template Matchings
           - [09] Overlapping Template Matchings
           - [10] Universal Statistical
           - [11] Approximate Entropy
           - [12] Random Excursions
           - [13] Random Excursions Variant
           - [14] Serial
           - [15] Linear Complexity

        
        For more information go 
        `here <https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-22r1a.pdf>`_.
        
        :param wait: bool indicating whether or not to wait for completion.
        :return: a dictionary of type :class:`.utils.resultNIST` if wait for 
            results else `.utils.StatusDict`
        :note: Occasional failures may occur for any given test. Only repeated failures for a given 
            test or many tests failing simulatenously indicate that the device entropy source is 
            malfunctioning.
        """
        health_resp = self.stub.HealthTest(
            uqrng_pb2.Empty()
        )
        if not wait:
            return message_to_dict(health_resp)
        # if chose to wait for completion
        start_health = self.FetchHealthTest()
        elapsed_time = start_health["test_detail"]["elapsed_time_mins"]
        while True:
            time.sleep(2)
            iter_health_res = self.FetchHealthTest()
            if iter_health_res["test_detail"]["elapsed_time_mins"]<elapsed_time:
                break
        return iter_health_res

    def FetchHealthTest(self) -> resultNIST:
        """
        Fetches most recent health test results from server

        :return: a dict of NIST testing results :class:`.resultNIST`
        """
        health_result = self.stub.FetchHealthTest(uqrng_pb2.Empty())
        health_detail = message_to_dict(health_result)
        if len(health_detail["passed"])!=0:
            summary_table = create_summary_table(detail_result=health_detail)
            return {
                "all_pass": all(health_detail["passed"]),
                "test_detail": health_detail,
                "summary_table": summary_table,
            }
        else:
            return {
                "all_pass": None,
                "test_detail": health_detail,
                "summary_table": ""
            }
        
        
    def ScheduleHealthTest(self, test_interval_mins: int) -> StatusDict:
        """
        Sets health test interval for running all health tests on the device.
        Results for scheduled health tests can be retrieved by calling
        :meth:`UqrngClient.FetchHealthTest`.

        :param test_interval_mins: the number of minutes between automated runs 
            for NIST-STS must be a positive integer if set to 0 indicates that 
            the user wishes to not run any further health checks while the 
            device is in operation. This is the default interval that is set on
            device startup.
        :return: a dict of class :class:`.utils.StatusDict` which indicates whether
            health test was successfully scheduled.
        :note: Restarting the device will remove any previous scheduling of 
            health tests set by users prior to powering down, the device will
            revert to it's default settings which is to run one health test at
            start up with no scheduled follow ups.
        """
        health_resp = self.stub.ScheduleHealthTest(
            uqrng_pb2.ScheduleInput(test_interval_mins=test_interval_mins)
        )
        return message_to_dict(health_resp)

    def SystemStatus(self)-> StatusDict:
        """
        Indicates whether the uQRNG device is idle or processing a request.

        :return: a member of :class:`.utils.SysStatus` of type 
            :class:`.utils.StatusDict`
        """
        status_resp = self.stub.SystemStatus(
            uqrng_pb2.Empty()
        )
        return message_to_dict(status_resp)

    def SystemInfo(self) -> SystemInfoDict:
        """
        Requests current system information.
        
        :return: a dict of type :class:`.utils.SystemInfoDict`
        """
        sys_info_resp = self.stub.SystemInfo(
            uqrng_pb2.Empty()
        )
        return message_to_dict(sys_info_resp)
