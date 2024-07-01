# uqrng-direct

This package is the companion client to Quantum Computing Inc.'s (QCi) Uniform Quantum Random Number Generator (uQRNG) hardware. uQRNG is a portable device that provides truly random numbers directly from a quantum process. High-quality entropy sources are essential for the seeding and creation of cryptographic keys. Other applications include fair selection (gaming and lotteries) and distribution in the blockchain, and unbiased randomness in simulations.

QCi’s uQRNG is a photonic technology that works by harvesting the entropy from the arrival time of single photons in a photonic circuit. Prior to detection, the arrival time of a single photon is in a state of superposition, that is the arrival time is truly random making it impossible to predict exactly at which point in time a photon will arrive at the detector. All the possible times for the photon arrival therefore exist in superposition with each other. QCi’s random number generator uses this quantum process to create high-dimensional quantum information which is then streamed to the client utilzing the interface provided within this package. QCi's uQRNG device has been rigorously tested to ensure that the randomness is of the highest quality. See our [white paper](https://quantumcomputinginc.com/learn/qrng/uqrng-whitepaper) regarding randomness validation for the device. Finally, if you'd like to learn more about how the uQRNG hardware works see our [research paper](https://opg.optica.org/ol/abstract.cfm?uri=ol-43-4-631)

## Additional Resources

- [Package documentation](https://quantumcomputinginc.com/learn/reference-documentation/uqrng-direct)
- [uQRNG Device Info](https://quantumcomputinginc.com/products/uqrng)
- [uQRNG Randomness Validation](https://quantumcomputinginc.com/learn/qrng/uqrng-whitepaper)
- [Programmable quantum random number generator without postprocessing](https://opg.optica.org/ol/abstract.cfm?uri=ol-43-4-631)
