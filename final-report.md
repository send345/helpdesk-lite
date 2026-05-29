# Итоговый отчёт по проекту HelpDesk Lite

## Цель проекта

Разработать backend-сервис для учёта заявок технической поддержки. Проект учебный, выполнен в рамках 4 спринтов.

## Что разработано

REST API для работы с заявками и комментариями. Сервис позволяет:

- создавать, просматривать, изменять заявки
- добавлять и просматривать комментарии
- фильтровать заявки по статусу и приоритету
- получать статистику по заявкам

## Использованный стек

| Компонент | Технология |
|-----------|------------|
| Язык | Python 3.11 |
| Фреймворк | FastAPI |
| База данных | PostgreSQL |
| ORM | SQLAlchemy |
| Валидация | Pydantic |
| Тесты | pytest |
| Контейнеризация | Docker, Docker Compose |
| Контроль версий | Git, GitHub |

## Архитектура приложения

Проект построен по принципу разделения ответственности:

- `main.py` — эндпоинты API
- `schemas.py` — Pydantic-схемы для валидации
- `crud.py` — функции работы с БД
- `models.py` — SQLAlchemy-модели
- `database.py` — подключение к PostgreSQL

Такая структура позволяет легко тестировать и расширять приложение.

## Схема базы данных

### Таблица `tickets`

| Поле | Тип | Описание |
|------|-----|----------|
| id | INTEGER | Первичный ключ |
| title | TEXT | Название заявки |
| description | TEXT | Описание проблемы |
| status | TEXT | new, in_progress, resolved, closed |
| priority | TEXT | low, medium, high, critical |
| author_name | TEXT | Автор заявки |
| assignee_name | TEXT | Исполнитель |
| created_at | TIMESTAMP | Дата создания |
| updated_at | TIMESTAMP | Дата изменения |

### Таблица `comments`

| Поле | Тип | Описание |
|------|-----|----------|
| id | INTEGER | Первичный ключ |
| ticket_id | INTEGER | Ссылка на заявку |
| author_name | TEXT | Автор комментария |
| text | TEXT | Текст комментария |
| created_at | TIMESTAMP | Дата создания |

Связь: `comments.ticket_id` → `tickets.id` (один ко многим)

## Описание API

| Метод | Путь | Описание |
|-------|------|----------|
| GET | `/health` | Проверка работы сервера |
| POST | `/tickets` | Создать заявку |
| GET | `/tickets` | Список заявок (фильтры: status, priority) |
| GET | `/tickets/{id}` | Получить одну заявку |
| PATCH | `/tickets/{id}` | Изменить статус/приоритет/исполнителя |
| POST | `/tickets/{id}/comments` | Добавить комментарий |
| GET | `/tickets/{id}/comments` | Получить комментарии |
| GET | `/stats/tickets` | Статистика по статусам заявок |

## Инструкция запуска проекта

### Локальный запуск

```bash
# Установить зависимости
pip install fastapi uvicorn sqlalchemy psycopg2-binary pytest python-dotenv

# Создать базу данных в PostgreSQL (название helpdesk_lite)

# Создать файл .env с переменной DATABASE_URL
# Пример: DATABASE_URL=postgresql://postgres:пароль@localhost/helpdesk_lite

# Создать таблицы
python init_db.py

# Запустить сервер
uvicorn main:app --reload

# Запуск через Docker
'''bash
docker compose up --build

После запуска сервер доступен по адресу: http://localhost:8000/docs


Инструкция запуска тестов
'''bash
python -m pytest
Результат: 12 passed


Перечень реализованных тестов
Файл	        		Что тестирует
test_main.py			/health и /hello
test_tickets.py		создание, список, получение, изменение заявок, обработку 404
test_comments.py	добавление и получение комментариев, пустые комментарии, проверку существования заявки
test_stats.py			статистику /stats/tickets
Всего тестов: 12 (позитивные и негативные сценарии). Результат: все проходят.


Основные проблемы, возникшие в ходе проекта:
1 Приложение в Docker не подключалось к БД — контейнер с приложением стартовал раньше, чем PostgreSQL.
Решение: добавил sleep 5 в command в docker-compose.yml

2Путаница между локальной БД и Docker-БД — создавал заявки в Docker, а смотрел локальную БД в PostgreSQL
Решение: научился проверять через docker exec


Выводы и предложения по развитию
Что удалось:
1 реализовать функциональность заявок и комментариев

2 Настроить Docker Compose для запуска приложения и базы данных

3 Написать тесты (12 штук)

4 Оформить документацию (README, final-report, db-schema, regression checklist)

5 Выложить код на GitHub с тегами по спринтам

