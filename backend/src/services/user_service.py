from fastapi import Depends
import bcrypt
from src.models import User
from src.repositories import UserRepository
from src.schemas.request import LoginRequest
from sqlalchemy.exc import NoResultFound

class UserService:
    def __init__(self, service: UserRepository = Depends()):
        self.service = service

    def login(self, request: LoginRequest) -> User | None:
        try:
            user = self.service.get_user_by_username(request.username)
            hashed_password = user.password

            byte_encoded_password = request.password.encode('utf-8')
            is_password_valid = bcrypt.checkpw(byte_encoded_password, hashed_password)
        except NoResultFound:
            return None

        return user if is_password_valid else None