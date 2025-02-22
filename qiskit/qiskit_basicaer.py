from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile
import time

def main():
    circuit = QuantumCircuit(1, 1)
    circuit.h(0)
    circuit.measure(0, 0)

    simulator = AerSimulator()
    start_time = time.time()
    transpiled_circuit = transpile(circuit, simulator)
    result = simulator.run(transpiled_circuit, shots=10_000).result()

    counts = result.get_counts()
    print("Resultados de medición:", counts)
    end_time = time.time()
    print(f"Qiskit: {end_time - start_time:.4f} segundos")

if __name__ == '__main__':
    main()
