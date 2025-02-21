# Simulación Cuántica con Qiskit, Cirq y PyQuil

Este repositorio contiene implementaciones de **tres simulaciones cuánticas** utilizando los frameworks **Qiskit, Cirq y PyQuil**.  
Cada programa ejecuta una **puerta Hadamard** en un qubit, lo mide y cuenta cuántas veces colapsa en `0` o `1`.  

---

## 📌 Estructura del Proyecto

- `qiskit_experiment.py` → Simulación usando **Qiskit**  
- `cirq_experiment.py` → Simulación usando **Cirq**  
- `pyquil_experiment.py` → Simulación usando **PyQuil**  
- `Dockerfile` → Configuración para ejecutar **PyQuil** en un contenedor Docker

---

## 🚀 Cómo Ejecutar los Experimentos

### **1️⃣ Ejecutar con Qiskit**
📌 **Requisitos:** Tener instalado **Python 3.11+** y `qiskit`.  

Ejecuta el siguiente comando en la terminal:
```sh
pip install qiskit
python qiskit_experiment.py
```

---

### **2️⃣ Ejecutar con Cirq**
📌 **Requisitos:** Tener instalado **Python 3.11+** y `cirq`.  

Ejecuta el siguiente comando en la terminal:
```sh
pip install cirq
python cirq_experiment.py
```

---

### **3️⃣ Ejecutar con PyQuil usando Docker**
📌 **Requisitos:** Tener instalado **Docker**.  

#### 🏗 **Construir la Imagen Docker**
```sh
docker build -t pyquil-experiment .
```

#### ▶️ **Ejecutar el Contenedor**
```sh
docker run --rm pyquil-experiment
```

🔹 **Salida esperada:**
```
Resultados de medición: {0: 5002, 1: 4998}
```

---