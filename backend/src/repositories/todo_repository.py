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