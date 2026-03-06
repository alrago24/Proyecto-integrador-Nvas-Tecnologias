# 🎓 Proyecto EduPerformance: Sistema de Gestión Académica

## 📘 1. Planteamiento del Caso de Estudio

### 1.1 Contexto y Problemática
En el ámbito educativo, los estudiantes a menudo carecen de herramientas centralizadas para monitorear su rendimiento en tiempo real. La dispersión de las calificaciones y la falta de un cálculo automático de promedios dificultan que el alumno identifique a tiempo las materias que requieren mayor refuerzo antes de finalizar el ciclo lectivo.

### 1.2 La Propuesta de Solución
**EduPerformance** es una aplicación de consola (inicialmente) desarrollada en Python que permite a los estudiantes gestionar su trayectoria académica de forma personalizada. El sistema ofrece:

* **Registro Dinámico:** El usuario define el número y nombre de las materias que cursará.
* **Gestión de Calificaciones:** Estructura el almacenamiento de 3 notas por cada asignatura inscrita.
* **Análisis de Desempeño:** Automatiza el cálculo de promedios por materia y genera un promedio general de la carrera.

### 1.3 Objetivo Técnico
El proyecto demuestra la implementación de estructuras de datos fundamentales (**Diccionarios y Listas**) y el control de flujo en Python, asegurando la integridad de la información y la facilidad de uso para el estudiante.


---

## 🛠️ 2. Requisitos del Entorno y Configuración

Para garantizar la portabilidad y el aislamiento de dependencias, este proyecto utiliza un entorno virtual de Python.

* **Lenguaje:** Python 3.10 o superior.
* **Dependencias:** Gestionadas mediante `requirements.txt`.
* **Entorno Virtual:** `venv`.

---

## 🚀 3. Guía de Instalación y Ejecución

Sigue estos pasos para configurar el proyecto en tu máquina local:

### 3.1 Clonar el repositorio
```bash
git clone [https://github.com/alrago24/Proyecto-integrador-Nvas-Tecnologias.git]
cd [Proyecto-integrador-nvas-Tecnologias]
```

### 3.2 Configurar el entorno Virtual(venv)

En Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

**Nota:** Si la ejecución de scripts está deshabilitada, usa:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 3.3 Instalar dependencias
Aunque el proyecto utiliza la biblioteca estándar de Python, es una buena práctica ejecutar:
```bash
pip install -r requirements.txt
```

### 3.4 Ejecutar la aplicación
```bash
python Archivo.py
```
---

## 📂 4. Estructura de Archivos
- `Archivo.py`: Contiene toda la lógica de registro, login y gestión de notas.
- `requirements.txt`: Archivo de dependencias para el despliegue.
- `.gitignore`: Configuración para excluir la carpeta `venv/` del repositorio.

---

## 5. Metodología GitFlow
El proyecto evidencia el uso de ramas para el desarrollo organizado:

- `main`: Versión final estable.
- `develop`: Integración de funcionalidades.
- `feature/`: Desarrollo de tareas especificas(lógica, configuración, promedios)
