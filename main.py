# Actualizar main.py (agregar solo al final)
from fastapi import FastAPI

app = FastAPI(title="Mi Primera API")

@app.get("/")
def hello_world():
    return {"message": "¡Mi primera API FastAPI!"}

@app.get("/info")
def info():
    return {"api": "FastAPI", "week": 1, "status": "running"}

# NUEVO: Endpoint personalizado (solo si hay tiempo)
@app.get("/greeting")
@app.get("/greeting/{name}")
def greet_user(name: str="Fernanda"):
    return {"greeting": f"¡Hola {name}!"}


@app.get("/my-profile")
def my_profile():
    return {
        "name": "Fernanda Betancourt",           # Cambiar por tu nombre
        "bootcamp": "FastAPI",
        "week": 1,
        "date": "14-08-2025",
        "likes_fastapi": True              # ¿Te gustó FastAPI?
    }