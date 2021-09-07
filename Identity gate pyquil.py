# Imports for pyQuil
import numpy as np
from pyquil import Program, get_qc
from pyquil.api import WavefunctionSimulator
from pyquil.gates import H, I, X, Y, Z, CNOT, MEASURE


# create a WavefunctionSimulator object and a generic QuantumComputer object
wavefunction_simulator = WavefunctionSimulator()
qc = get_qc('9q-generic-qvm')

# pyQuil is based around operations (or gates) so we will start with the most
# basic one: the identity operation, called I. I takes one argument, the index
# of the qubit that it should be applied to.
# Make a quantum program that allocates one qubit (qubit #0) and does nothing to it
p = Program(I(0))

# Quantum states are called wavefunctions for historical reasons.
# We can run this basic program on our connection to the simulator.
# This call will return the state of our qubits after we run program p.
# This api call returns a tuple, but we'll ignore the second value for now.
wavefunction = wavefunction_simulator.wavefunction(p)

# wavefunction is a Wavefunction object that stores a quantum state as a list of amplitudes
alpha, beta = wavefunction

print("Our qubit is in the state alpha={} and beta={}".format(alpha, beta))
print("The probability of measuring the qubit in outcome 0 is {}".format(abs(alpha)**2))
print("The probability of measuring the qubit in outcome 1 is {}".format(abs(beta)**2))

p = Program(I(0))
results = qc.run_and_measure(p, trials=10)[0]

print(results)
