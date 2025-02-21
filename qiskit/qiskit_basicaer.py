from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile

def main():
    circuit = QuantumCircuit(1, 1)
    circuit.h(0)
    circuit.measure(0, 0)

    simulator = AerSimulator()  # Simulador sin necesidad de Aer
    transpiled_circuit = transpile(circuit, simulator)
    result = simulator.run(transpiled_circuit, shots=10_000).result()

    counts = result.get_counts()
    print("Resultados de medición:", counts)

if __name__ == '__main__':
    main()
