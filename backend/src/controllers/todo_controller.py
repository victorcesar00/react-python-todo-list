from fastapi import APIRouter, Depends
from src.schemas.request import CreateTodoRequest, UpdateTodoRequest
from src.schemas.response import TodoResponse
from src.services import TodoService

router = APIRouter()

@router.post("")
async def create_todo(todo: CreateTodoRequest, service: TodoService = Depends()) -> TodoResponse:
    return service.create_todo(todo)

@router.put("")
async def update_todo(todo: UpdateTodoRequest, service: TodoService = Depends()) -> TodoResponse:
    return service.update_todo(todo)

@router.delete("/{todo_id}")
async def delete_todo(todo_id: int, service: TodoService = Depends()) -> None:
    service.delete_todo(todo_id)