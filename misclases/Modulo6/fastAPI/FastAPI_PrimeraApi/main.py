from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/curso')
async def curso():
    return {"message": "Curso de FastAPI"}

