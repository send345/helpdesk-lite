from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from crud import get_tickets, get_ticket, create_ticket, update_ticket
from schemas import TicketCreate, TicketResponse, TicketUpdate
from schemas import CommentCreate, CommentResponse
from crud import get_comments, create_comment
import logging
from crud import get_stats

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Зависимость для получения сессии БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/health')
def health_check():
    return {'status': 'ok'}

@app.get('/hello')
def say_hello(name: str):
    return {'message': f'Hello, {name}'}

# --- API для заявок ---

@app.post('/tickets', response_model=TicketResponse)
def create_new_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    logger.info(f"Creating new ticket: {ticket.title}")
    return create_ticket(db, ticket)

@app.get('/tickets', response_model=list[TicketResponse])
def list_tickets(status: str = None, priority: str = None, db: Session = Depends(get_db)):
    return get_tickets(db, status, priority)

@app.get('/tickets/{ticket_id}', response_model=TicketResponse)
def get_one_ticket(ticket_id: int, db: Session = Depends(get_db)):
    db_ticket = get_ticket(db, ticket_id)
    if not db_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return db_ticket

@app.patch('/tickets/{ticket_id}', response_model=TicketResponse)
def update_one_ticket(ticket_id: int, ticket_update: TicketUpdate, db: Session = Depends(get_db)):
    logger.info(f"Updating ticket {ticket_id}")
    db_ticket = update_ticket(db, ticket_id, ticket_update)
    if not db_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return db_ticket

@app.post('/tickets/{ticket_id}/comments', response_model=CommentResponse)
def add_comment(ticket_id: int, comment: CommentCreate, db: Session = Depends(get_db)):
    logger.info(f"Adding comment to ticket {ticket_id}")
    # Проверяем, существует ли заявка
    ticket = get_ticket(db, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    # Запрещаем пустой комментарий
    if not comment.text or not comment.text.strip():
        raise HTTPException(status_code=400, detail="Comment text cannot be empty")
    return create_comment(db, ticket_id, comment)

@app.get('/tickets/{ticket_id}/comments', response_model=list[CommentResponse])
def list_comments(ticket_id: int, db: Session = Depends(get_db)):
    # Проверяем, существует ли заявка
    ticket = get_ticket(db, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return get_comments(db, ticket_id)

@app.get('/stats/tickets')
def get_ticket_stats(db: Session = Depends(get_db)):
    return get_stats(db)