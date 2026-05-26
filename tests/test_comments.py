from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add_comment():
    # Сначала создадим заявку
    ticket = client.post("/tickets", json={
        "title": "Для комментария",
        "description": "Описание",
        "author_name": "Тестер"
    })
    ticket_id = ticket.json()["id"]
    
    # Добавим комментарий
    response = client.post(f"/tickets/{ticket_id}/comments", json={
        "author_name": "Тестер",
        "text": "Тестовый комментарий"
    })
    assert response.status_code == 200
    assert response.json()["text"] == "Тестовый комментарий"

def test_get_comments():
    # Создадим заявку
    ticket = client.post("/tickets", json={
        "title": "Для списка комментариев",
        "description": "Описание",
        "author_name": "Тестер"
    })
    ticket_id = ticket.json()["id"]
    
    # Добавим комментарий
    client.post(f"/tickets/{ticket_id}/comments", json={
        "author_name": "Тестер",
        "text": "Первый"
    })
    
    # Получим список
    response = client.get(f"/tickets/{ticket_id}/comments")
    assert response.status_code == 200
    assert len(response.json()) >= 1

def test_empty_comment():
    # Создадим заявку
    ticket = client.post("/tickets", json={
        "title": "Для пустого комментария",
        "description": "Описание",
        "author_name": "Тестер"
    })
    ticket_id = ticket.json()["id"]
    
    # Попробуем добавить пустой комментарий
    response = client.post(f"/tickets/{ticket_id}/comments", json={
        "author_name": "Тестер",
        "text": ""
    })
    assert response.status_code == 400

def test_comment_to_nonexistent_ticket():
    response = client.post("/tickets/99999/comments", json={
        "author_name": "Тестер",
        "text": "Комментарий"
    })
    assert response.status_code == 404