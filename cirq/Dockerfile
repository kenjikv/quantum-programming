# Usa Python 3.11 como imagen base
FROM python:3.11

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instala Cirq en el contenedor
RUN pip install --no-cache-dir cirq

# Copia el código fuente al contenedor
COPY cirq_experiment.py /app/cirq_experiment.py

# Comando de ejecución
CMD ["python", "cirq_experiment.py"]
