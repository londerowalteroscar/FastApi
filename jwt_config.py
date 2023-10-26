from jwt import encode, decode

def dame_token(dato:dict)->str:
    token:str = encode(payload=dato, key="mi_clave", algorithm="HS256")
    return token

def valida_token(token:dict)->dict:
    dato:dict = decode(token,  key="mi_clave", algorithm=["HS256"])
    return dato