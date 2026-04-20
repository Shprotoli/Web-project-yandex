# API V1

## Auth
- `POST /auth/register` — регистрация пользователя
- `POST /auth/login` — вход и создание сессии
- `POST /auth/logout` — выход из текущей сессии по Bearer token
- `POST /auth/logout-all` — завершение всех сессий пользователя

## Users
- `GET /users` — список пользователей
- `GET /users/<user_id>` — пользователь по id
- `GET /users/me` — текущий пользователь по Bearer token
- `GET /users/<user_id>/sessions` — сессии пользователя

## Sessions
- `GET /sessions` — список всех сессий
- `GET /sessions/<session_id>` — сессия по id
- `DELETE /sessions/<session_id>` — удалить сессию
- `DELETE /sessions/expired` — удалить все истёкшие сессии

## Blitzes
- `GET /blitzes` — список blitz
- `POST /blitzes` — создать blitz
- `GET /blitzes/<blitz_id>` — получить blitz
- `PUT /blitzes/<blitz_id>` — полное обновление blitz
- `PATCH /blitzes/<blitz_id>` — частичное обновление blitz
- `DELETE /blitzes/<blitz_id>` — удалить blitz

## Service
- `GET /health` — healthcheck
