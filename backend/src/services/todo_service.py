from fastapi import Depends
from src.repositories import TodoRepository
from src.schemas.request import CreateTodoRequestSchema, UpdateTodoRequestSchema
from src.models import Todo

class TodoService:
    def __init__(self, repository: TodoRepository = Depends()):
        self.repository = repository

    def create_todo(self, user_id: int, todo: CreateTodoRequestSchema) -> Todo:
        todo_to_insert = Todo(**todo.model_dump())
        todo_to_insert.user_id = user_id

        inserted_todo = self.repository.insert(todo_to_insert)

        return inserted_todo

    def update_todo(self, todo: UpdateTodoRequestSchema) -> Todo:
        todo_to_update = Todo(**todo.model_dump())

        updated_todo = self.repository.update(todo_to_update)

        return updated_todo
    
    def delete_todo(self, todo_id: int) -> bool:
        return self.repository.delete(todo_id)

    def get_todos_by_user_id(self, user_id: int) -> list[Todo]:
        return self.repository.get_by_user_id(user_id)