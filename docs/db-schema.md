# Схема базы данных HelpDesk Lite

## Таблица `tickets` (заявки)

| Поле | Тип | Описание |
|------|-----|----------|
| `id` | INTEGER | Первичный ключ, автоинкремент |
| `title` | TEXT | Название заявки (обязательное) |
| `description` | TEXT | Описание проблемы (обязательное) |
| `status` | TEXT | Статус: `new`, `in_progress`, `resolved`, `closed` |
| `priority` | TEXT | Приоритет: `low`, `medium`, `high`, `critical` |
| `author_name` | TEXT | Автор заявки (обязательное) |
| `assignee_name` | TEXT | Исполнитель (опционально) |
| `created_at` | TIMESTAMP | Дата и время создания |
| `updated_at` | TIMESTAMP | Дата и время последнего изменения |

## Таблица `comments` (комментарии)

| Поле | Тип | Описание |
|------|-----|----------|
| `id` | INTEGER | Первичный ключ, автоинкремент |
| `ticket_id` | INTEGER | Ссылка на заявку (внешний ключ к `tickets.id`) |
| `author_name` | TEXT | Автор комментария (обязательное) |
| `text` | TEXT | Текст комментария (обязательное, не пустой) |
| `created_at` | TIMESTAMP | Дата и время создания |

## Связи между таблицами
Одна заявка может иметь много комментариев.  
Связь реализована через поле `comments.ticket_id`, которое ссылается на `tickets.id`.

Таблицы создаются через SQLAlchemy в файле init_db.py:

python
Base.metadata.create_all(bind=engine)
Модели описаны в models.py:

Ticket — таблица tickets

Comment — таблица comments
