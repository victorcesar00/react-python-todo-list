from fastapi import Depends, HTTPException, status
from typing import List
from src.repositories.interfaces import TodoRepositoryInterface
from src.repositories import TodoRepository
from src.schemas.request import CreateTodoRequestSchema, UpdateTodoRequestSchema
from src.models import Todo

class TodoService:
    def __init__(self, repository: TodoRepositoryInterface = Depends(TodoRepository)):
        self.repository = repository

    def create_todo(self, user_id: int, todo: CreateTodoRequestSchema) -> Todo:
        todo_to_insert = Todo(**todo.model_dump())
        todo_to_insert.user_id = user_id

        inserted_todo = self.repository.insert(todo_to_insert)

        return inserted_todo

    def update_todo(self, user_id: int, todo: UpdateTodoRequestSchema) -> Todo:
        todo_to_update = self.repository.get(todo.id)

        if not todo_to_update:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='To-do not found')

        if todo_to_update.user_id != user_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='To-do doesn\'t belong to user')

        todo_to_update.description = todo.description

        updated_todo = self.repository.update(todo_to_update)

        return updated_todo
    
    def delete_todo(self, user_id: int, todo_id: int) -> bool:
        todo_to_delete = self.repository.get(todo_id)

        if not todo_to_delete:
            return False

        if todo_to_delete.user_id != user_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='To-do doesn\'t belong to user')

        return self.repository.delete(todo_id)

    def get_todos_by_user_id(self, user_id: int) -> List[Todo]:
        return self.repository.get_by_user_id(user_id)