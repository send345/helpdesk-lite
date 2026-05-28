from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# ПОДСТАВЬ СВОЙ ПАРОЛЬ вместо postgres
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:5556666775@localhost/helpdesk_lite")
SQLALCHEMY_DATABASE_URL = DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()