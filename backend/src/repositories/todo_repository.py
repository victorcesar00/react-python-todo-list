from fastapi import Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Todo

class TodoRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
    
    def insert(self, todo: Todo) -> Todo:
        self.db.add(todo)
        self.db.commit()
        self.db.refresh(todo)

        return todo
    
    def update(self, todo: Todo) -> Todo:
        todo_on_db: Todo = self.db.get(Todo, todo.id)
        todo_on_db.description = todo.description

        self.db.commit()
        self.db.refresh(todo_on_db)

        return todo_on_db

    def delete(self, todo_id: int) -> None:
        self.db.query(Todo).filter(Todo.id == todo_id).delete()
        self.db.commit()