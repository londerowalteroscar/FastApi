from fastapi import FastAPI

# Crear instancia de FastAPI
app = FastAPI()

# Titulo de la Aplicación de FastAPI
app.title = "Tutorial FastApi"

# Versión de la Aplicación de FastAPI
app.version = "1.0.1"

# Crear punto de entreada o endpoint:
@app.get("/", tags = ["Bienvenida"]) # Cambio de etiqueta en documentación.
def mensaje():
    mensaje = "Bienvenido Walter!"
    return mensaje
