from abc import ABC, abstractmethod
from typing import List
from src.schemas.request import CreateTodoRequestSchema, UpdateTodoRequestSchema
from src.models import Todo

class TodoServiceInterface(ABC):
    @abstractmethod
    def create_todo(self, user_id: int, todo: CreateTodoRequestSchema) -> Todo:
        pass

    @abstractmethod
    def update_todo(self, user_id: int, todo: UpdateTodoRequestSchema) -> Todo:
        pass

    @abstractmethod
    def delete_todo(self, user_id: int, todo_id: int) -> bool:
        pass

    @abstractmethod
    def get_todos_by_user_id(self, user_id: int) -> List[Todo]:
        pass
