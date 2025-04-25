from pydantic import BaseModel

class Cliente(BaseModel):
    nombre: str
    edad: int

class ClienteResponse(BaseModel):
    msg: str
    result: dict 