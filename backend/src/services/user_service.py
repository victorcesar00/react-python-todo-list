from fastapi import Depends
import bcrypt
from src.models import User
from src.repositories import UserRepository
from src.schemas.request import LoginRequestSchema
from sqlalchemy.exc import NoResultFound

class UserService:
    def __init__(self, repository: UserRepository = Depends()):
        self.repository = repository

    def login(self, request: LoginRequestSchema) -> User | None:
        try:
            user = self.repository.get_user_by_username(request.username)
            hashed_password = user.password

            byte_encoded_password = request.password.encode('utf-8')
            password_is_valid = bcrypt.checkpw(byte_encoded_password, hashed_password)
        except NoResultFound:
            return None

        return user if password_is_valid else None
    
    def get_user(self, user_id) -> User | None:
        try:
            return self.repository.get(user_id)
        except NoResultFound:
            return None