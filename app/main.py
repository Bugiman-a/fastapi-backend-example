from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="FastAPI Backend Example")

class Item(BaseModel):
    name: str
    price: float

@app.get("/")
async def root():
    return {"status": "ok"}

@app.post("/items")
async def create_item(item: Item):
    return {"item": item}
