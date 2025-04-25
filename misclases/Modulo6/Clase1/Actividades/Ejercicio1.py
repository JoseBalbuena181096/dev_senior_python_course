from fastapi import FastAPI
import uvicorn
from routes import router

app = FastAPI(
    title="API de Clientes",
    description="API para gestionar clientes",
    version="1.0.0"
)

app.include_router(router, prefix="/api")

if __name__ == "__main__":
    # al localhost:8000/docs se puede acceder al API documentation
    uvicorn.run(app, host="localhost", port=8000)