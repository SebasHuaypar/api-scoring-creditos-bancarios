from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import re

# Configuramos la app de FastAPI
app = FastAPI(
    title="API de Scoring Crediticio",
    description="Microservicio para evaluación automática de créditos bancarios.",
    version="1.0.0"
)

# Definimos el modelo de datos de entrada
class SolicitudCredito(BaseModel):
    ingreso_mensual: str  
    deuda_total: str      
    historial_crediticio: str 
    edad: int

# Reusamos las clases hechas en el proyecto de Colab
class DataIngestion:
    def __init__(self, df: pd.DataFrame):
        self.df = df
    
    def limpiar_datos_numericos(self, columna: str):
        self.df[columna] = self.df[columna].astype(str).str.replace(r"S/\.|,", "", regex=True).astype(float)

class FeatureEngineering:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def procesar(self):
        self.df["ratio_dti"] = self.df["deuda_total"] / self.df["ingreso_mensual"]
        mapping = {"Bueno": 3, "Malo": 0, "Nulo": 1}
        self.df["historial_score"] = self.df["historial_crediticio"].map(mapping)
        self.df = self.df.fillna(0)
        return self.df

# Entrenamos el modelo al inicio (simulación)
print("Entrenando modelo inicial...")
datos_dummy = {
    "ingreso_mensual": [5000, 1000, 8000, 2000, 10000, 1200] * 20,
    "deuda_total": [1000, 800, 1000, 1500, 2000, 900] * 20,
    "historial_score": [3, 0, 3, 1, 3, 0] * 20,
    "edad": [30, 25, 45, 22, 50, 20] * 20
}
df_train = pd.DataFrame(datos_dummy)
df_train["ratio_dti"] = df_train["deuda_total"] / df_train["ingreso_mensual"]
df_train["target"] = ((df_train["ratio_dti"] < 0.40) & (df_train["historial_score"] > 0)).astype(int)

X_train = df_train[["ingreso_mensual", "deuda_total", "edad", "ratio_dti", "historial_score"]]
y_train = df_train["target"]

modelo = RandomForestClassifier(n_estimators=10, random_state=42)
modelo.fit(X_train, y_train)
print("Modelo cargado y listo.")

# Configuramos los endpoints de la API
@app.get("/")
def home():
    return {"mensaje": "Bienvenido al Sistema de Scoring del BCP (Simulado). Ve a /docs para probar."}

@app.post("/predecir")
def predecir_credito(solicitud: SolicitudCredito):
    datos = {
        "ingreso_mensual": [solicitud.ingreso_mensual],
        "deuda_total": [solicitud.deuda_total],
        "historial_crediticio": [solicitud.historial_crediticio],
        "edad": [solicitud.edad]
    }
    df = pd.DataFrame(datos)

    ingesta = DataIngestion(df)
    ingesta.limpiar_datos_numericos("ingreso_mensual")
    ingesta.limpiar_datos_numericos("deuda_total")
    df_limpio = ingesta.df

    ingenieria = FeatureEngineering(df_limpio)
    df_final = ingenieria.procesar()

    features = ["ingreso_mensual", "deuda_total", "edad", "ratio_dti", "historial_score"]
    X_input = df_final[features]

    prediccion = modelo.predict(X_input)[0] 
    probabilidad = modelo.predict_proba(X_input)[0][1] 

    estado = "APROBADO" if prediccion == 1 else "RECHAZADO"
    
    return {
        "cliente_edad": solicitud.edad,
        "estado": estado,
        "probabilidad_aprobacion": round(probabilidad, 2),
        "mensaje": "Crédito pre-aprobado automáticamente" if estado == "APROBADO" else "No cumple políticas de riesgo"
    }