from fastapi import FastAPI
import uvicorn
from routers.items import router as items_router

# Crear la instancia de la aplicación FastAPI
app = FastAPI()
app.include_router(items_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
















