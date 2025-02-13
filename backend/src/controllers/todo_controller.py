from fastapi import APIRouter, Depends
from src.schemas.request import CreateTodoRequestSchema, UpdateTodoRequestSchema
from src.schemas.response import TodoResponseSchema
from src.services import TodoService

router = APIRouter()

@router.post("")
async def create_todo(todo: CreateTodoRequestSchema, service: TodoService = Depends()) -> TodoResponseSchema:
    return service.create_todo(todo)

@router.put("")
async def update_todo(todo: UpdateTodoRequestSchema, service: TodoService = Depends()) -> TodoResponseSchema:
    return service.update_todo(todo)

@router.delete("/{todo_id}")
async def delete_todo(todo_id: int, service: TodoService = Depends()) -> None:
    service.delete_todo(todo_id)