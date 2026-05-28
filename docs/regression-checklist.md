# Regression Checklist (проверка, что ничего не сломалось)

## Заявки (tickets)
- [ ] Создать заявку — POST /tickets → 200, данные сохранились
- [ ] Получить список всех заявок — GET /tickets → 200, список не пустой
- [ ] Получить одну заявку — GET /tickets/1 → 200, данные верные
- [ ] Фильтр по статусу — GET /tickets?status=new → только новые
- [ ] Фильтр по приоритету — GET /tickets?priority=high → только high
- [ ] Изменить статус — PATCH /tickets/1 {"status":"resolved"} → статус изменился
- [ ] Изменить приоритет — PATCH /tickets/1 {"priority":"critical"} → приоритет изменился
- [ ] Ошибка 404 — GET /tickets/999 → 404

## Комментарии (comments)
- [ ] Добавить комментарий — POST /tickets/1/comments → 200
- [ ] Получить комментарии — GET /tickets/1/comments → 200
- [ ] Пустой комментарий — POST с text="" → 400
- [ ] Комментарий к несуществующей заявке → 404

## Статистика (stats)
- [ ] Статистика по статусам — GET /stats/tickets → 200, есть поля new, in_progress и т.д.

## Базовые проверки
- [ ] Health check — GET /health → 200, {"status":"ok"}
- [ ] Swagger открывается — http://localhost:8000/docs
- [ ] Тесты проходят — pytest → 11+ passed

## Docker (если запускаешь через Docker)
- [ ] Контейнеры поднялись — docker ps (2 контейнера)
- [ ] Swagger работает — http://localhost:8000/docs
- [ ] API работают так же, как локально