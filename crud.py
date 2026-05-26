from sqlalchemy.orm import Session
from models import Ticket
from schemas import TicketCreate, TicketUpdate
from models import Comment
from schemas import CommentCreate

# Получить все заявки (с фильтрами)
def get_tickets(db: Session, status: str = None, priority: str = None):
    query = db.query(Ticket)
    if status:
        query = query.filter(Ticket.status == status)
    if priority:
        query = query.filter(Ticket.priority == priority)
    return query.all()

# Получить одну заявку по id
def get_ticket(db: Session, ticket_id: int):
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()

# Создать новую заявку
def create_ticket(db: Session, ticket: TicketCreate):
    db_ticket = Ticket(
        title=ticket.title,
        description=ticket.description,
        author_name=ticket.author_name,
        priority=ticket.priority,
        assignee_name=ticket.assignee_name
    )
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

# Обновить заявку
def update_ticket(db: Session, ticket_id: int, ticket_update: TicketUpdate):
    db_ticket = get_ticket(db, ticket_id)
    if not db_ticket:
        return None
    
    update_data = ticket_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_ticket, key, value)
    
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

# Получить все комментарии заявки
def get_comments(db: Session, ticket_id: int):
    return db.query(Comment).filter(Comment.ticket_id == ticket_id).all()

# Создать комментарий
def create_comment(db: Session, ticket_id: int, comment: CommentCreate):
    db_comment = Comment(
        ticket_id=ticket_id,
        author_name=comment.author_name,
        text=comment.text
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment