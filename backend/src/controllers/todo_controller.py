from fastapi import APIRouter, Depends, Request, Response, HTTPException
from typing import Union
from src.schemas.request import CreateTodoRequestSchema, UpdateTodoRequestSchema
from src.schemas.response import TodoResponseSchema, ErrorResponseSchema
from src.services import TodoService
from src.services.interfaces import TodoServiceInterface
from src.limiter import limiter

router = APIRouter()

def get_service(service: TodoServiceInterface = Depends(TodoService)) -> TodoServiceInterface:
    return service

@router.post('', response_model=TodoResponseSchema)
@limiter.limit('5/second')
async def create_todo(todo: CreateTodoRequestSchema, request: Request, service: TodoServiceInterface = Depends(get_service)):
    return service.create_todo(request.user['id'], todo)

@router.put('', response_model=Union[TodoResponseSchema, ErrorResponseSchema])
@limiter.limit('5/second')
async def update_todo(todo: UpdateTodoRequestSchema, request: Request, response: Response, service: TodoServiceInterface = Depends(get_service)):
    try:
        return service.update_todo(request.user['id'], todo)
    except HTTPException as e:
        response.status_code = e.status_code

        return ErrorResponseSchema(message = e.detail)

@router.delete('/{todo_id}', response_model=Union[bool, ErrorResponseSchema])
@limiter.limit('5/second')
async def delete_todo(todo_id: int, request: Request, response: Response, service: TodoServiceInterface = Depends(get_service)):
    try:
        return service.delete_todo(request.user['id'], todo_id)
    except HTTPException as e:
        response.status_code = e.status_code

        return ErrorResponseSchema(message = e.detail)

@router.get('/user', response_model=list[TodoResponseSchema])
@limiter.limit('5/second')
async def get_user_todos(request: Request, service: TodoServiceInterface = Depends(get_service)):
    return service.get_todos_by_user_id(request.user['id'])