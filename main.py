from fastapi import FastAPI

# Crear instancia de FastAPI
app = FastAPI()

# Crear punto de entreada o endpoint:
@app.get("/")
def mensaje():
    mensaje = "Bienvenido Walter!"
    return mensaje
