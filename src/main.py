import random
from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Estudante(BaseModel):
    name: str
    curso: str
    ativo: bool


@app.get("/helloworld")
def read_root():
    return {"Hello": "World"}

#127.7.7.1:8000/teste1
@app.get("/teste1")
async def funcaoteste():
    return {"teste": True, "num_Aleatorio": random.randint(0, 4000)}


@app.post("/estudantes/cadastro")
async def create_estudante(estudante: Estudante):
    return estudante

@app.put("/estudantes/update/{id_estudante}")
async def update_estudante(id_estudante: int):
    return id_estudante > 0

@app.delete ("/estudantes/delete/{id_estudante}")
async def delete_estudante(id_estudante: int)
    return id_estudante > 0