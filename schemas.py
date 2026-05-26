from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Схема для создания заявки (POST /tickets)
class TicketCreate(BaseModel):
    title: str
    description: str
    author_name: str
    priority: Optional[str] = "medium"
    assignee_name: Optional[str] = ""

# Схема для ответа (GET /tickets, GET /tickets/{id})
class TicketResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str
    priority: str
    author_name: str
    assignee_name: str
    created_at: datetime
    updated_at: datetime

# Схема для изменения заявки (PATCH /tickets/{id})
class TicketUpdate(BaseModel):
    status: Optional[str] = None
    priority: Optional[str] = None
    assignee_name: Optional[str] = None

# Схема для создания комментария
class CommentCreate(BaseModel):
    author_name: str
    text: str

# Схема для ответа с комментарием
class CommentResponse(BaseModel):
    id: int
    ticket_id: int
    author_name: str
    text: str
    created_at: datetime