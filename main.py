from fastapi import FastAPI
from fastapi.responses import HTMLResponse
# Crear instancia de FastAPI
app = FastAPI()

# Titulo de la Aplicación de FastAPI
app.title = "Tutorial FastApi"

# Versión de la Aplicación de FastAPI
app.version = "1.0.1"

# Diccionario de pruebas
ventas = [
    {
        "id": 1,
        "fecha": "12/02/2022",
        "tienda": "Malena",
        "importe": 22.000
    },
    {
        "id": 2,
        "fecha": "13/02/2022",
        "tienda": "Mauri",
        "importe": 44.000
    }
]
# Crear punto de entreada o endpoint:
@app.get("/", tags = ["Bienvenida"]) # Cambio de etiqueta en documentación.
def mensaje():
    return HTMLResponse("<h2> Titulo HTML desde FastApi </h2>")

@app.get("/ventas", tags = ["Ventas"])
def dame_ventas():
    return ventas

@app.get("/ventas/{id}", tags = ["Ventas"])
def dame_ventas (id:int):
    for elem in ventas:
        if elem["id"]==id:
            return elem
    return []

@app.get("/ventas/", tags = ["Ventas"])
def dame_ventas_por_tienda(tienda:str): 
    return [elem for elem in ventas if elem["tienda"]==tienda]

