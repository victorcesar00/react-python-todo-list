from abc import ABC, abstractmethod
from src.models import User

class UserRepositoryInterface(ABC):

    @abstractmethod
    def get_user_by_username(self, username: str) -> User:
        pass