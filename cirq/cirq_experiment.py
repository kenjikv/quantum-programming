import cirq
import time

def main():
    # Creamos un qubit
    qubit = cirq.LineQubit(0)

    start_time = time.time()

    # Creamos un circuito cuántico
    circuit = cirq.Circuit()

    # Aplicamos la puerta Hadamard para poner el qubit en superposición
    circuit.append(cirq.H(qubit))

    # Medimos el qubit
    circuit.append(cirq.measure(qubit, key='m'))

    # Simulamos el circuito cuántico
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=10_000)

    end_time = time.time()

    # Obtenemos y mostramos los resultados
    counts = result.histogram(key='m')
    print("Resultados de medición:", counts)
    print(f"Cirq: {end_time - start_time:.4f} segundos")

if __name__ == '__main__':
    main()
