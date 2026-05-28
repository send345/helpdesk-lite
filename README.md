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

```bash(терминал)
git config --global user.name "Твое Имя"
git config --global user.email "tvoy@email.com"
cd helpdesk-lite
2. Установить библиотеки
'''bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary pytest
3. Настроить базу данных
Открой pgAdmin (устанавливается вместе с PostgreSQL)

Создай новую базу данных с именем helpdesk_lite

В файле database.py укажи свой пароль в строке:

python(файл-python)
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:твой_пароль@localhost/helpdesk_lite"
4. Создать таблицы
'''bash
python init_db.py
Если нет ошибок — таблица tickets создана.

5. Запустить сервер
'''bash
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
POST /tickets/1/comments	Добавить комментарий к заявке
GET /tickets/1/comments	Посмотреть комментарии заявки
GET /stats/tickets	Статистика: сколько заявок в каждом статусе
Статусы заявки
new → in_progress → resolved → closed

Приоритеты
low → medium → high → critical

Как проверить, что всё работает
'''bash
python -m pytest
Результат должен быть  таким: 11 passed

Как работали с Git
Каждую новую функцию сохраняли отдельным коммитом

В конце каждого спринта ставили тег:
git tag sprint-1
git tag sprint-2
git tag sprint-3
git tag sprint-4
git tag final

Что сделано по спринтам
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

Спринт 3
Создали таблицу comments для комментариев

Добавили API: POST /tickets/{id}/comments и GET /tickets/{id}/comments

Запретили пустые комментарии и комментарии к несуществующим заявкам

Написали тест-кейсы (14 шт) и баг-репорты (3 шт) в папке docs/

Написали автотесты для комментариев

Добавили логирование (программа пишет в терминал, что делает)

Поставили тег sprint-3

Спринт 4
Добавили статистику /stats/tickets

Написали Dockerfile и docker-compose.yml

Теперь проект можно запустить одной командой: docker compose up --build

Написали итоговый отчёт final-report.md

Поставили теги sprint-4 и final




 Запуск через Docker (всё одной командой)
Если у тебя установлен Docker Desktop, проект запускается без установки Python и PostgreSQL:

bash
docker compose up --build
После запуска открывай: http://localhost:8000/docs





helpdesk-lite/
├── main.py           # Главный файл с эндпоинтами
├── database.py       # Подключение к PostgreSQL
├── models.py         # Описание таблиц (Ticket, Comment)
├── schemas.py        # Форматы данных (Pydantic)
├── crud.py           # Функции работы с БД
├── init_db.py        # Создание таблиц
├── tests/
│   ├── test_main.py
│   ├── test_tickets.py
│   └── test_comments.py
├── docs/
│   ├── test-cases.md
│   ├── bug-reports.md
│   └── join-query.sql
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── README.md
└── final-report.md