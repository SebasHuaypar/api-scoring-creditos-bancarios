# CREDIT SCORING API | MICROSERVICIO DE RIESGO FINANCIERO

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95%2B-009688)
![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

## Descripción del Proyecto
Este proyecto implementa una **API RESTful** para la evaluación automática de riesgo crediticio en tiempo real. 

A diferencia de los modelos tradicionales estáticos, este microservicio permite a aplicaciones externas (Web, App Móvil) enviar datos de solicitantes y recibir una decisión de aprobación instantánea basada en un modelo de **Machine Learning (Random Forest)**.

El sistema simula la arquitectura backend de una entidad bancaria moderna, integrando validación de datos, pipelines de limpieza y lógica de negocio.

## Características Técnicas
* **Arquitectura Cliente-Servidor:** Separación lógica entre la simulación bancaria y el motor de decisión.
* **Validación Robusta:** Uso de **Pydantic** para asegurar la integridad de los datos de entrada (Tipado estricto).
* **Hot-Reloading:** Despliegue con **Uvicorn** para alta disponibilidad durante el desarrollo.
* **ML Pipeline Integrado:** Limpieza de datos (ETL) y Feature Engineering ejecutados al vuelo en cada petición.
* **Documentación Automática:** Swagger UI interactivo generado automáticamente.

## Tecnologías Usadas
* **Python 3.10+**
* **FastAPI:** Framework moderno de alto rendimiento para construcción de APIs.
* **Uvicorn:** Servidor ASGI.
* **Scikit-Learn:** Motor de Machine Learning.
* **Pandas/Numpy:** Manipulación de datos vectorizada.

## Instalación y Ejecución Local

Sigue estos pasos para levantar el microservicio en tu máquina:

### 1. Clonar el repositorio
```bash
git clone [https://github.com/SebasHuaypar/api-scoring-creditos-bancarios.git](https://github.com/SebasHuaypar/api-scoring-creditos-bancarios.git)
cd api-scoring-creditos-bancarios
```
### 2. Crear entorno virtual (Recomendado)
```bash
python -m venv venv
# En Windows:
.\venv\Scripts\activate
# En Mac/Linux:
source venv/bin/activate
```
3. Instalar dependencias
```bash
pip install -r requirements.txt
```
4. Levantar el Servidor (API)
```bash
uvicorn main:app --reload
El servidor iniciará en: http://127.0.0.1:8000
```
5. Probar el Cliente (Simulación)
En una nueva terminal, ejecuta el script que simula el sistema bancario enviando solicitudes:
```bash
python cliente_bancario.py
```
## Documentación de la API (Swagger)
Con el servidor corriendo, visita http://127.0.0.1:8000/docs para ver la documentación interactiva y probar los endpoints manualmente.

## Estructura del Proyecto
```plaintext
/
├── main.py                # Código fuente del Servidor (API + Modelo ML)
├── cliente_bancario.py    # Script de simulación de cliente (Frontend simulado)
├── requirements.txt       # Lista de dependencias del proyecto
└── README.md              # Documentación
```
