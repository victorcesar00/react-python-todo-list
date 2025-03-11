from fastapi import APIRouter, Depends, Request, Response, HTTPException
from src.schemas.request import CreateTodoRequestSchema, UpdateTodoRequestSchema
from src.schemas.response import TodoResponseSchema, ErrorResponseSchema
from src.services import TodoService

router = APIRouter()

@router.post('')
async def create_todo(todo: CreateTodoRequestSchema, request: Request, service: TodoService = Depends()) -> TodoResponseSchema:
    return service.create_todo(request.user['id'], todo)

@router.put('')
async def update_todo(todo: UpdateTodoRequestSchema, request: Request, response: Response, service: TodoService = Depends()) -> TodoResponseSchema | ErrorResponseSchema:
    try:
        return service.update_todo(request.user['id'], todo)
    except HTTPException as e:
        response.status_code = e.status_code

        return ErrorResponseSchema(message = e.detail)

@router.delete('/{todo_id}')
async def delete_todo(todo_id: int, request: Request, response: Response, service: TodoService = Depends()) -> bool | ErrorResponseSchema:
    try:
        return service.delete_todo(request.user['id'], todo_id)
    except HTTPException as e:
        response.status_code = e.status_code

        return ErrorResponseSchema(message = e.detail)

@router.get('/user')
async def get_user_todos(request: Request, service: TodoService = Depends()) -> list[TodoResponseSchema]:
    return service.get_todos_by_user_id(request.user['id'])