from fastapi import Depends
from typing import Optional, List
from sqlalchemy.orm import Session
from src.repositories.interfaces import TodoRepositoryInterface
from src.database import get_db
from src.models import Todo

class TodoRepository(TodoRepositoryInterface):
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
    
    def get(self, id: int) -> Optional[Todo]:
        return self.db.query(Todo).filter(Todo.id == id).first()

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

    def delete(self, id: int) -> bool:
        deletion_success = self.db.query(Todo).filter(Todo.id == id).delete()
        self.db.commit()

        return deletion_success

    def get_by_user_id(self, user_id) -> List[Todo]:
        return self.db.query(Todo).filter(Todo.user_id == user_id).all()