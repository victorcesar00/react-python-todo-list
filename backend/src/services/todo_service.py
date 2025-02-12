from fastapi import Depends
from src.repositories import TodoRepository
from src.schemas.request import CreateTodoRequest, UpdateTodoRequest
from src.models import Todo

class TodoService:
    def __init__(self, repository: TodoRepository = Depends()):
        self.repository = repository

    def create_todo(self, todo: CreateTodoRequest) -> Todo:
        todo_to_insert = Todo(**todo.model_dump())

        inserted_todo = self.repository.insert(todo_to_insert)

        return inserted_todo

    def update_todo(self, todo: UpdateTodoRequest) -> Todo:
        todo_to_update = Todo(**todo.model_dump())

        updated_todo = self.repository.update(todo_to_update)

        return updated_todo
    
    def delete_todo(self, todo_id: int) -> None:
        self.repository.delete(todo_id)