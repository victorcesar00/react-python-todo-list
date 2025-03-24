from abc import ABC, abstractmethod
from typing import Optional, List
from src.models import Todo

class TodoRepositoryInterface(ABC):

    @abstractmethod
    def get(self, id: int) -> Optional[Todo]:
        pass
    
    @abstractmethod
    def insert(self, todo: Todo) -> Todo:
        pass
    
    @abstractmethod
    def update(self, todo: Todo) -> Todo:
        pass
    
    @abstractmethod
    def delete(self, id: int) -> bool:
        pass
    
    @abstractmethod
    def get_by_user_id(self, user_id) -> List[Todo]:
        pass