from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel

from database import SessionLocal, TodoItem

app = FastAPI()

# Pydantic-схемы (для валидации данных)
class TodoCreate(BaseModel):
    title: str
    description: str = ""

class TodoResponse(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

# Функция для получения сессии БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "To-Do API работает!"}

@app.get("/todos", response_model=List[TodoResponse])
def get_todos(db: Session = Depends(get_db)):
    return db.query(TodoItem).all()

@app.post("/todos", response_model=TodoResponse)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    new_todo = TodoItem(title=todo.title, description=todo.description)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(TodoItem).filter(TodoItem.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    db.delete(todo)
    db.commit()
    return {"message": f"Задача {todo_id} удалена"}

@app.put("/todos/{todo_id}/complete")
def complete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(TodoItem).filter(TodoItem.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    todo.completed = True
    db.commit()
    db.refresh(todo)
    return todo