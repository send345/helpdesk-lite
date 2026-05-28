from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_stats():
    # Сначала создадим пару заявок
    client.post("/tickets", json={
        "title": "Стат 1",
        "description": "Описание",
        "author_name": "Тестер"
    })
    client.post("/tickets", json={
        "title": "Стат 2",
        "description": "Описание",
        "author_name": "Тестер"
    })
    
    # Проверим статистику
    response = client.get("/stats/tickets")
    assert response.status_code == 200
    data = response.json()
    assert "new" in data  # есть поле new
    assert isinstance(data["new"], int)  # значение — число