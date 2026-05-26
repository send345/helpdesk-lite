-- Получить все заявки вместе с их комментариями
SELECT 
    tickets.id AS ticket_id,
    tickets.title,
    tickets.status,
    comments.id AS comment_id,
    comments.author_name,
    comments.text,
    comments.created_at AS comment_created_at
FROM tickets
LEFT JOIN comments ON tickets.id = comments.ticket_id
ORDER BY tickets.id, comments.created_at;