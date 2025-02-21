import cirq

def main():
    # Creamos un qubit
    qubit = cirq.LineQubit(0)

    # Creamos un circuito cuántico
    circuit = cirq.Circuit()

    # Aplicamos la puerta Hadamard para poner el qubit en superposición
    circuit.append(cirq.H(qubit))

    # Medimos el qubit
    circuit.append(cirq.measure(qubit, key='m'))

    # Simulamos el circuito cuántico
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=10_000)

    # Obtenemos y mostramos los resultados
    counts = result.histogram(key='m')
    print("Resultados de medición:", counts)

if __name__ == '__main__':
    main()
