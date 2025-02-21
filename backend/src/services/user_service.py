from fastapi import Depends
from dotenv import load_dotenv
from sqlalchemy.exc import NoResultFound
from typing import Union
import os
import bcrypt
import jwt
import json
from datetime import datetime, timedelta, timezone
from src.models import User
from src.repositories import UserRepository
from src.schemas.request import LoginRequestSchema
from src.schemas.response import Token

load_dotenv()

HASHING_SECRET_KEY = os.getenv('HASHING_SECRET_KEY')
HASHING_ALGORITHM = os.getenv('HASHING_ALGORITHM')

class UserService:
    def __init__(self, repository: UserRepository = Depends()):
        self.repository = repository

    def _authenticate_user(self, request: LoginRequestSchema) -> Union[User, False]:
        try:
            user = self.repository.get_user_by_username(request.username)
            hashed_password = user.password

            byte_encoded_password = request.password.encode('utf-8')
            password_is_valid = bcrypt.checkpw(byte_encoded_password, hashed_password)

            return user if password_is_valid else False
        except NoResultFound:
            return False
    
    @staticmethod
    def _create_access_token(user: User) -> Token:
        expiration_date = datetime.now(timezone.utc) + timedelta(days=1)

        data_to_encode = {
            'id': user.id,
            'username': user.username,
        }

        data_to_encode_as_json = json.dumps(data_to_encode)

        encode_object={'sub': data_to_encode_as_json, 'exp': expiration_date}
        jwt_token = jwt.encode(encode_object, HASHING_SECRET_KEY, algorithm=HASHING_ALGORITHM)

        return Token(access_token=jwt_token)

    def login(self, request: LoginRequestSchema) -> Union[Token, None]:
        user = self._authenticate_user(request)

        if not user:
            return None
        
        access_token = self._create_access_token(user)

        return access_token
    
    def get_user(self, user_id) -> User | None:
        try:
            return self.repository.get(user_id)
        except NoResultFound:
            return None