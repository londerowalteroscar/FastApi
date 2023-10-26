from jwt import encode, decode
import jwt 
def dame_token(dato:dict)->str:
    token:str = encode(payload=dato, key="mi_clave", algorithm="HS256")
    return token

def valida_token(token):
    dato: dict = jwt.decode(token, key="mi_clave", algorithms=["HS256"])
    return dato

