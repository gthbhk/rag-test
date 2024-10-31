from fastapi import APIRouter
from pydantic import BaseModel
import uvicorn

router = APIRouter()


class Item(BaseModel):
    name: str
    price: int


@router.get("/items/{item_name}")
def get_item(item_name: str):
    return {"name": item_name, "price": 200}


@router.post("/items/new")
def add_item(item: Item):
    return item


@router.get("/call_aoai")
def call_aoai():
    return {"result": "aoai called"}


if __name__ == "__main__":
    uvicorn.run(router, host="0.0.0.0", port=8080)
