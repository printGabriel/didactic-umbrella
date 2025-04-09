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


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


#127.7.7.1:8000/teste1
@app.get("/teste1")
async def funcaoteste():
    return {"teste": True, "num_Aleatorio": random.randint(0, 2000)}

@app.post("/estudantes/cadastro")
async def create_estudante(estudante: Estudante):
    return estudante

@app.put("/estudantes/update/{id_estudante}")
async def update_item(item_estudante: int):
    return id_estudante > 0

@app.delete ("/estudantes/delete/{id_estudante}")
async def delete_estudante(id_estudante: int)
return id_estudante > 0