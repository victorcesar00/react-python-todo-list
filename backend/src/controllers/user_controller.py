from fastapi import APIRouter, Depends, Response, status
from src.schemas.request import LoginRequestSchema
from src.schemas.response import UserResponseSchema
from src.schemas.response import ErrorResponseSchema
from src.services import UserService

router = APIRouter()

@router.post('/login')
async def login(request: LoginRequestSchema, response: Response, service: UserService = Depends()) -> UserResponseSchema | ErrorResponseSchema:
    user = service.login(request)

    if user:
        return user

    response.status_code = status.HTTP_401_UNAUTHORIZED

    return ErrorResponseSchema(message = 'Credenciais inválidas')

@router.get('/{user_id}')
async def getUser(user_id: int, response: Response, service: UserService = Depends()) -> UserResponseSchema | ErrorResponseSchema:
    user = service.get_user(user_id)

    if user:
        return user

    response.status_code = status.HTTP_404_NOT_FOUND

    return ErrorResponseSchema(message = 'Usuário não cadastrado')