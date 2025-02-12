from fastapi import APIRouter, Depends
from src.schemas.request import CreateTodoRequest
from src.schemas.response import TodoCreatedResponse
from src.services import TodoService

router = APIRouter()

@router.post("")
async def create_todo(todo: CreateTodoRequest, service: TodoService = Depends()) -> TodoCreatedResponse:
    return service.create_todo(todo)