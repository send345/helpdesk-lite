from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from crud import get_tickets, get_ticket, create_ticket, update_ticket
from schemas import TicketCreate, TicketResponse, TicketUpdate

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
    db_ticket = update_ticket(db, ticket_id, ticket_update)
    if not db_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return db_ticket