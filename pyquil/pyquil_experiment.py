from pyquil import Program
from pyquil.gates import H, MEASURE
from pyquil.api import QuantumComputer
from pyquil.pyqvm import PyQVM
import numpy as np

def main():
    # Crear un programa cuántico
    program = Program()

    # Declarar un registro de memoria clásico donde se almacenarán los resultados de medición
    ro = program.declare("ro", memory_type="BIT", memory_size=1)

    # Aplicar la puerta Hadamard al qubit 0
    program += H(0)

    # Medir el qubit y almacenar el resultado en la memoria clásica
    program += MEASURE(0, ro[0])

    # Configurar el programa para ejecutarse 10 000 veces (shots)
    program.wrap_in_numshots_loop(10_000)

    # Configurar PyQVM como simulador cuántico sin compilador
    simulator = QuantumComputer(
        name="pyqvm",  # Nombre del simulador
        qam=PyQVM(n_qubits=1),  # Simulador de 1 qubit
        compiler=None  # No se necesita compilador en el simulador
    )

    # Ejecutar el programa cuántico en el simulador
    result = simulator.run(program)

    # Obtener los datos de medición desde la memoria clásica
    raw_measurements = result.get_register_map()["ro"]

    # Convertir los resultados en un array de NumPy para facilitar el conteo
    measurements = np.array(raw_measurements).astype(int).flatten()

    # Contar las ocurrencias de los resultados ('0' y '1')
    unique, counts = np.unique(measurements, return_counts=True)
    counts_dict = dict(zip(unique, counts))

    # Mostrar los resultados de medición en la terminal
    print("Resultados de medición:", counts_dict)

if __name__ == '__main__':
    main()
