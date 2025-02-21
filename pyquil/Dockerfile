# Usa Python 3.11 como imagen base
FROM python:3.11

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instala PyQuil y las dependencias necesarias
RUN pip install --no-cache-dir pyquil numpy

# Copia el código fuente al contenedor
COPY pyquil_experiment.py /app/pyquil_experiment.py

# Comando de ejecución
CMD ["python", "pyquil_experiment.py"]
