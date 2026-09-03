# FastAPI To-Do API

Простое API для управления списком задач (To-Do) на **FastAPI** с использованием **SQLite**.

## 🚀 Функционал

- ✅ Создание задачи (`POST /todos`)
- ✅ Просмотр всех задач (`GET /todos`)
- ✅ Отметка задачи как выполненной (`PUT /todos/{id}/complete`)
- ✅ Удаление задачи (`DELETE /todos/{id}`)

## 🛠️ Технологии

- Python 3.14
- FastAPI
- SQLAlchemy
- SQLite
- Swagger UI (автодокументация)

## 📦 Установка и запуск

```bash
# Установка зависимостей
pip install fastapi uvicorn sqlalchemy

# Запуск сервера
uvicorn main:app --reload