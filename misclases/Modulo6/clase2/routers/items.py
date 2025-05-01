from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/items", tags=["items"])

class Item(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    impuesto: Optional[float] = None

items = [
    {"nombre": "Item 1", "descripcion": "Descripción del item 1", "precio": 100, "impuesto": 10},
    {"nombre": "Item 2", "descripcion": "Descripción del item 2", "precio": 200, "impuesto": 20},
    {"nombre": "Item 3", "descripcion": "Descripción del item 3", "precio": 300, "impuesto": 30},
]

@router.get("/{item_id}")
async def read_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

@router.post("/")
async def create_item(item: Item):
    items.append(item)
    return item

@router.get("/")
async def list_items():
    return items

@router.put("/{item_id}")
async def update_item(item_id: int, item: Item):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    return item

@router.delete("/{item_id}")
async def delete_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    deleted_item = items.pop(item_id)
    return {"message": "Item eliminado", "item": deleted_item} 