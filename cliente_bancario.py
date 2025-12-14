import requests
import json

# Definimos la URL del endpoint de la API
URL = "http://127.0.0.1:8000/predecir"

# Simulamos 3 clientes que entran a la web del banco
clientes_nuevos = [
    {
        "ingreso_mensual": "S/. 8,500",
        "deuda_total": "S/. 500",
        "historial_crediticio": "Bueno",
        "edad": 30
    },
    {
        "ingreso_mensual": "S/. 1,200", 
        "deuda_total": "S/. 5,000",     
        "historial_crediticio": "Malo",
        "edad": 45
    },
    {
        "ingreso_mensual": "S/. 15,000",
        "deuda_total": "S/. 200",
        "historial_crediticio": "Bueno",
        "edad": 25
    }
]

# Iniciamos el sistema bancario (simulación) y conectamos con la API
print("Sistema bancario iniciado.")
print("Conectando con la API...")

for i, cliente in enumerate(clientes_nuevos):
    print(f"Procesando Cliente #{i+1}...")
    
    try:
        respuesta = requests.post(URL, json=cliente)
        
        if respuesta.status_code == 200:
            datos = respuesta.json()
            estado = datos["estado"]
            prob = datos["probabilidad_aprobacion"] * 100
            
            if estado == "APROBADO":
                print(f"¡APROBADO! (Probabilidad: {prob}%)")
            else:
                print(f"RECHAZADO. (Probabilidad: {prob}%)")
            print(f"   Mensaje: {datos['mensaje']}")
            
        else:
            print(f"Error en la API: {respuesta.text}")
            
    except Exception as e:
        print(f"No se pudo conectar con la API. ¿Está prendido el servidor? Error: {e}")
        
    print("-" * 30)