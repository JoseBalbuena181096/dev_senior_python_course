from fastapi import APIRouter, HTTPException
from models import Cliente, ClienteResponse

router = APIRouter()

# Datos de ejemplo (en una aplicación real, esto vendría de una base de datos)
CLIENTES = [
    {"nombre": "Juan", "edad": 30},
    {"nombre": "Maria", "edad": 25},
    {"nombre": "Pedro", "edad": 35},
    {"nombre": "Ana", "edad": 28}
]

@router.post("/cliente", response_model=ClienteResponse)
async def crear_cliente(cliente: Cliente):
    # Aquí iría la lógica para insertar en la base de datos
    CLIENTES.append({
        "nombre": cliente.nombre,
        "edad": cliente.edad
    })
    return {
        "msg": "El cliente se ha creado correctamente",
        "result": {
            "nombre": cliente.nombre,
            "edad": cliente.edad
        }
    }

@router.get("/clientes", response_model=ClienteResponse)
async def obtener_clientes():
    return {
        "msg": "Los clientes se han obtenido",
        "result": {
            "clientes": CLIENTES
        }
    }

@router.get("/cliente/{nombre}", response_model=ClienteResponse)
async def obtener_cliente(nombre: str):
    cliente = next((c for c in CLIENTES if c["nombre"] == nombre), None)
    if not cliente:
        raise HTTPException(
            status_code=404,
            detail={
                "msg": "Cliente no encontrado",
                "result": {}
            }
        )
    return {
        "msg": "Cliente encontrado",
        "result": cliente
    }

@router.put("/cliente/{nombre}", response_model=ClienteResponse)
async def actualizar_cliente(nombre: str, cliente: Cliente):
    cliente_existente = next((c for c in CLIENTES if c["nombre"] == nombre), None)
    if not cliente_existente:
        raise HTTPException(
            status_code=404,
            detail={
                "msg": "Cliente no encontrado",
                "result": {}
            }
        )
    cliente_existente["nombre"] = cliente.nombre
    cliente_existente["edad"] = cliente.edad
    return {
        "msg": "Cliente actualizado correctamente",
        "result": {
            "nombre": cliente.nombre,
            "edad": cliente.edad
        }
    }

@router.delete("/cliente/{nombre}", response_model=ClienteResponse)
async def eliminar_cliente(nombre: str):
    # verificamos si el cliente existe
    cliente_existente = next((c for c in CLIENTES if c["nombre"] == nombre), None)
    if not cliente_existente:
        raise HTTPException(
            status_code=404,
            detail={
                "msg": "Cliente no encontrado",
                "result": {}
            }
        )
    # eliminamos el cliente
    CLIENTES[:] = [c for c in CLIENTES if c["nombre"] != nombre]
    return {
        "msg": "Cliente eliminado correctamente",
        "result": {
            "clientes": CLIENTES
        }
    }   

