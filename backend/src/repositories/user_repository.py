from fastapi import Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import User

class UserRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
        

    def get_user_by_username(self, username: str) -> User:
        return self.db.query(User).filter(User.username == username).one()
