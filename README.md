# HelpDesk Lite

Это учебный проект — простая система заявок для техподдержки.  
Программа умеет создавать заявки, просматривать их, менять статус и приоритет.

---

## Что нужно установить перед запуском

- **Python** (версия 3.11 или новее) — скачать с python.org  
- **Git** — скачать с git-scm.com  
- **PostgreSQL** — скачать с postgresql.org

---

## Как скачать и запустить проект

### 1. Скопировать репозиторий

Открой терминал и выполни:

```bash
git config --global user.name "Твое Имя"
git config --global user.email "tvoy@email.com"
cd helpdesk-lite
2. Установить библиотеки
bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary pytest
3. Настроить базу данных
Открой pgAdmin (устанавливается вместе с PostgreSQL)

Создай новую базу данных с именем helpdesk_lite

В файле database.py укажи свой пароль в строке:

python
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:твой_пароль@localhost/helpdesk_lite"
4. Создать таблицы
bash
python init_db.py
Если нет ошибок — таблица tickets создана.

5. Запустить сервер
bash
uvicorn main:app --reload
Открой браузер и перейди по адресу:
👉 http://localhost:8000/docs

Ты увидишь документацию и сможешь тестировать все команды прямо в браузере.

Что умеет программа
Адрес	Что делает
GET /health	Проверка, работает ли сервер
POST /tickets	Создать заявку
GET /tickets	Список всех заявок
GET /tickets?status=new	Список с фильтром по статусу
GET /tickets/1	Показать заявку с номером 1
PATCH /tickets/1	Изменить статус, приоритет или исполнителя
Статусы заявки
new → in_progress → resolved → closed

Приоритеты
low → medium → high → critical

Как проверить, что всё работает
bash
pytest
Результат должен быть примерно таким: 7 passed

Как работали с Git
Каждую новую функцию сохраняли отдельным коммитом

В конце каждого спринта ставили тег:
git tag sprint-1
git tag sprint-2

Что сделано за первые два спринта
Спринт 1

Установили Python, Git, редактор кода

Создали репозиторий и README

Написали приложение на FastAPI с эндпоинтами /health и /hello

Добавили тесты

Поставили тег sprint-1

Спринт 2

Установили PostgreSQL, создали базу данных helpdesk_lite

Создали таблицу tickets

Написали API для заявок: создание, список, одна заявка, изменение

Добавили фильтры по статусу и приоритету

Добавили обработку ошибки (заявка не найдена)

Написали тесты

Поставили тег sprint-2

Структура проекта
text
helpdesk-lite/
├── main.py           # Главный файл с эндпоинтами
├── database.py       # Подключение к PostgreSQL
├── models.py         # Описание таблиц
├── schemas.py        # Форматы данных (Pydantic)
├── crud.py           # Функции работы с БД
├── init_db.py        # Создание таблиц
├── tests/
│   ├── test_main.py
│   └── test_tickets.py
├── README.md