import random
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

#127.7.7.1:8000/teste1
@app.get("/teste1")
async def funcaoteste():
    return {"teste": True, "num_Aleatorio": random.randint(0, 2000)};