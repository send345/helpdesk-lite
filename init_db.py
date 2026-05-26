from database import engine
from models import Base

print("Создаём таблицы...")
Base.metadata.create_all(bind=engine)
print("Готово!")