# Usa Python 3.11 como base
FROM python:3.11

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instala Qiskit con soporte para AerSimulator
RUN pip install --no-cache-dir qiskit qiskit-aer

# Copia el código fuente al contenedor
COPY qiskit_basicaer.py /app/qiskit_basicaer.py

# Comando de ejecución
CMD ["python", "qiskit_basicaer.py"]
