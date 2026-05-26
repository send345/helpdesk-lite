from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_ticket():
    response = client.post("/tickets", json={
        "title": "Тест",
        "description": "Описание",
        "author_name": "Тестер",
        "priority": "high"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Тест"
    assert data["status"] == "new"

def test_get_tickets():
    response = client.get("/tickets")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_one_ticket():
    # Сначала создадим заявку
    create = client.post("/tickets", json={
        "title": "Для поиска",
        "description": "Описание",
        "author_name": "Тестер"
    })
    ticket_id = create.json()["id"]
    
    # Теперь получим её
    response = client.get(f"/tickets/{ticket_id}")
    assert response.status_code == 200
    assert response.json()["id"] == ticket_id

def test_update_ticket():
    # Создадим
    create = client.post("/tickets", json={
        "title": "Для изменения",
        "description": "Описание",
        "author_name": "Тестер"
    })
    ticket_id = create.json()["id"]
    
    # Изменим статус
    response = client.patch(f"/tickets/{ticket_id}", json={
        "status": "in_progress"
    })
    assert response.status_code == 200
    assert response.json()["status"] == "in_progress"

def test_get_not_found():
    response = client.get("/tickets/99999")
    assert response.status_code == 404