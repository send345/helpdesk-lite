from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ПОДСТАВЬ СВОЙ ПАРОЛЬ вместо postgres
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:5556666775@localhost/helpdesk_lite"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()