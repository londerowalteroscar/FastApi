from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import Optional

# Crear instancia de FastAPI
app = FastAPI()

# Titulo de la Aplicación de FastAPI
app.title = "Tutorial FastApi"

# Versión de la Aplicación de FastAPI
app.version = "1.0.1"

# Creamos el Modelo:
class Ventas(BaseModel):
    id: int = Field(ge=0, le=20)
    # id: Optional[int]=None
    fecha:str
    tienda: str = Field(default="Malena", min_lenght=4, max_lenght=10)
    # tienda:str
    importe:float
        
    class Config:
        schema_extra = {
            "example" : {
                "id":5,
                "fecha":"01/01/2021",
                "tienda":"WALTER",
                "importe":20
            }
        }    
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
#----------------------------------------------------------------
# Crear punto de entreada o endpoint:
@app.get("/", tags = ["Bienvenida"]) # Cambio de etiqueta en documentación.
def mensaje():
    return HTMLResponse("<h2> Titulo HTML desde FastApi </h2>")


#----------------------------------------------------------------
@app.get("/ventas", tags = ["Ventas"])
def dame_ventas():
    return ventas


#----------------------------------------------------------------
@app.get("/ventas/{id}", tags = ["Ventas"])
def dame_ventas (id:int = Path(ge=1, le=1000)):
    for elem in ventas:
        if elem["id"]==id:
            return elem
    return []


#----------------------------------------------------------------
@app.get("/ventas/", tags = ["Ventas"])
def dame_ventas_por_tienda(tienda:str = Query(min_length=4, max_length=20)): 
    return [elem for elem in ventas if elem["tienda"]==tienda]

#----------------------------------------------------------------
# Esta función me premite colocar en la API datos que luego se agregaran a "ventas".
# Dicha funcion lo guarda en la variable y queda en memoria, pero podriamos guardarlo en un archivo 
# sin problemas.

@app.post("/ventas", tags=["Ventas"])
def crea_venta(venta:Ventas):
    ventas.append(venta)
    return ventas

#----------------------------------------------------------------
# Esta función realiza cambios en el diccionario que elegimos a traves del id.

@app.put("/ventas/{id}", tags=["Ventas"])
def actualiza_ventas(id:int, venta:Ventas):
    # Recorrer elementos de una lista.
    for elem in ventas:
        if elem["id"] == id:
            elem["fecha"] = venta.fecha
            elem["tienda"] = venta.tienda
            elem["importe"] = venta.importe
    return ventas

#----------------------------------------------------------------
# Esta función Elimina a un elemento de un diccionario por id.

@app.delete("/ventas/{id}", tags=["Ventas"])
def borra_venta(id:int):
    # Recorremos los elementos de la lista.
    for elem in ventas:
        if elem["id"] == id:
            ventas.remove(elem)
    return ventas

#----------------------------------------------------------------
