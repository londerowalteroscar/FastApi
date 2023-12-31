from fastapi import FastAPI, Body, Path, Query, HTTPException, Depends, Request
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from jwt_config import dame_token, valida_token
from fastapi.security import HTTPBearer
import jwt



# Crear instancia de FastAPI
app = FastAPI()

# Titulo de la Aplicación de FastAPI
app.title = "Tutorial FastApi"

# Versión de la Aplicación de FastAPI
app.version = "1.0.1"


#Modelo Usuario
class Usuario(BaseModel):
    email:str
    clave:str
    
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

class Portador(HTTPBearer):
    async def __call__(self, request: Request):
        autorizacion = await super().__call__(request)
        dato = valida_token(autorizacion.credentials)
        if dato["email"] != "londer@gmail.com":
            raise HTTPException(status_code=403, detail="Not authorized")
        
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
    },
    {
        "id": 3,
        "fecha": "13/02/2022",
        "tienda": "Brasilero",
        "importe": 50.000
    },
    {
        "id": 4,
        "fecha": "13/02/2022",
        "tienda": "Paisa",
        "importe": 14.000
    }
]
#----------------------------------------------------------------
# Crear punto de entreada o endpoint:
@app.get("/", tags=["Bienvenida"]) 
def mensaje():
    content = (
        "<h2> Bienvenido a la <a href='http://127.0.0.1:8000/docs#/' > FastAPI </a> </h2>"
    )
    return HTMLResponse(content)


#----------------------------------------------------------------
@app.get("/ventas", tags = ["Ventas"], response_model = List[Ventas], status_code = 200, dependencies=[Depends(Portador())])
def dame_ventas()->List[Ventas]:
    return JSONResponse(content = ventas)


#----------------------------------------------------------------
@app.get("/ventas/{id}", tags = ["Ventas"], response_model = Ventas, status_code = 200)
def dame_ventas (id:int = Path(ge=1, le=1000))-> ventas:
    for elem in ventas:
        if elem["id"]==id:
            return JSONResponse(content = elem, status_code = 200)
    return JSONResponse(content = [], status_code = 404)


#----------------------------------------------------------------
@app.get("/ventas/", tags = ["Ventas"], response_model = List[Ventas], status_code = 200)
def dame_ventas_por_tienda(tienda:str = Query(min_length=4, max_length=20))->List[Ventas]:
    datos = [elem for elem in ventas if elem["tienda"]==tienda]
    return JSONResponse(content = datos, status_code = 200)

#----------------------------------------------------------------
# Esta función me premite colocar en la API datos que luego se agregaran a "ventas".
# Dicha funcion lo guarda en la variable y queda en memoria, pero podriamos guardarlo en un archivo 
# sin problemas.

@app.post("/ventas", tags=["Ventas"], response_model = dict, status_code = 201)
def crea_venta(venta:Ventas) -> dict:
    ventas.append(dict (venta))
    return JSONResponse(content = {"Mensaje": "Venta Registrada"}, status_code = 200)

#----------------------------------------------------------------
# Esta función realiza cambios en el diccionario que elegimos a traves del id.

@app.put("/ventas/{id}", tags=["Ventas"], response_model = dict, status_code = 201)
def actualiza_ventas(id:int, venta:Ventas) -> dict:
    # Recorrer elementos de una lista.
    for elem in ventas:
        if elem["id"] == id:
            elem["fecha"] = venta.fecha
            elem["tienda"] = venta.tienda
            elem["importe"] = venta.importe
    return JSONResponse(content = {"Mensaje": "Venta Actualizada"})

#----------------------------------------------------------------
# Esta función Elimina a un elemento de un diccionario por id.

@app.delete("/ventas/{id}", tags=["Ventas"], response_model = dict, status_code = 200)
def borra_venta(id:int) -> dict:
    # Recorremos los elementos de la lista.
    for elem in ventas:
        if elem["id"] == id:
            ventas.remove(elem)
    return JSONResponse(content = {"Mensaje": "Venta Borrada"})

#----------------------------------------------------------------
# Creamos Ruta para LogIn
@app.post("/Login", tags=["Autenticación"])
def login(usuario: Usuario):
    if usuario.email == "londer@gmail.com" and usuario.clave == "2236":
        # Obtenemos el token con la funcion pasandole el diccionario de usuario.
        token = dame_token(usuario.dict())
        return JSONResponse(status_code=200, content={"token": token})
    else:
        raise HTTPException(status_code=404, detail="Acceso denegado.")