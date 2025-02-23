from fastapi import APIRouter, Depends, Request
from src.schemas.request import CreateTodoRequestSchema, UpdateTodoRequestSchema
from src.schemas.response import TodoResponseSchema
from src.services import TodoService

router = APIRouter()

@router.post('')
async def create_todo(todo: CreateTodoRequestSchema, request: Request, service: TodoService = Depends()) -> TodoResponseSchema:
    return service.create_todo(request.user['id'], todo)

@router.put('')
async def update_todo(todo: UpdateTodoRequestSchema, service: TodoService = Depends()) -> TodoResponseSchema:
    return service.update_todo(todo)

@router.delete('/{todo_id}')
async def delete_todo(todo_id: int, service: TodoService = Depends()) -> bool:
    return service.delete_todo(todo_id)

@router.get('/user')
async def get_user_todos(request: Request, service: TodoService = Depends()) -> list[TodoResponseSchema]:
    return service.get_todos_by_user_id(request.user['id'])