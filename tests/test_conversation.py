from fastapi.testclient import TestClient
# from src.main import app
from src.business_logic import conversation

client = TestClient(conversation.router)


def test_get_item():
    response = client.get("/items/item_a")
    assert response.status_code == 200
    assert response.json() == {"name": "item_a", "price": 200}

# TODO: AOAIレスポンスをモック使ったテストを追加する

# main.pyのテスト時のコード
# client = TestClient(app)

# def test_get_item():
#     response = client.get("/items/item_a")
#     assert response.status_code == 200
#     assert response.json() == {"name": "item_a", "price": 200}
