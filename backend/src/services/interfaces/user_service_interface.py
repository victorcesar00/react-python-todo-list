from typing import Union
from abc import ABC, abstractmethod
from src.schemas.request import LoginRequestSchema
from src.schemas.response import Token
from src.models import User

class UserServiceInterface(ABC):

    @abstractmethod
    def _authenticate_user(self, request: LoginRequestSchema) -> Union[User, False]:
        pass
    
    @abstractmethod
    def _create_access_token(user: User) -> Token:
        pass
    
    @abstractmethod
    def login(self, request: LoginRequestSchema) -> Union[Token, None]:
        pass