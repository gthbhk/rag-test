import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.openapi.utils import get_openapi

app = FastAPI()


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="カスタムタイトルのテストです",
        version="0.0.1",
        description="これはカスタムのOpenAPIスキーマです",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


class Item(BaseModel):
    name: str
    price: int

@app.get("/items/{item_name}",
         summary="アイテムの取得",
         description="アイテムの名前を指定して取得します",
         )
def get_item(item_name):
    return {"name": item_name, "price": 200}


@app.post("/items/new",
          summary="アイテムの追加",
          description="アイテムを追加します",
          )
def add_item(item: Item):
    return item


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
