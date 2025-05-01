# import fastapi
from fastapi import FastAPI
# import pydantic para crear modelos
from pydantic import BaseModel

app = FastAPI()

# Iniciar el servidor
# uvicorn users:app --reload

# Crear un modelo de un usuario
class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int

# una lista de usuarios
users = [
    User(id=1, name="John", surname="Doe", age=30),
    User(id=2, name="Jane", surname="Doe", age=25),
    User(id=3, name="Bob", surname="Doe", age=35),
]
    
@app.get("/users")
async def get_users():
    return [user.model_dump() for user in users]

# Obtener un usuario por path 
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return [user.model_dump() for user in users if user.id == user_id]

# Obtener un usuario por query
@app.get("/user/")
async def get_user(user_id: int):
    print(user_id)
    return [user.model_dump() for user in users if user.id == user_id]

# Buscar por id y nombre por path 
@app.get("/user/{user_id}/{name}")
async def get_user(user_id: int, name: str):
    return [user.model_dump() for user in users if user.id == user_id and user.name == name]

# Buscar por id y nombre por query
@app.get("/user/")
async def get_user(user_id: int, name: str):
    return [user.model_dump() for user in users if user.id == user_id and user.name == name]

@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return user 

@app.put("/users/{user_id}")
async def update_user(user_id: int, user_update: User):
    for index, user in enumerate(users):
        if user.id == user_id:
            users[index] = user_update
            return users[index]
    return {"error": "User not found"}

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user.id == user_id:
            return users.pop(index)
    return {"error": "User not found"}

