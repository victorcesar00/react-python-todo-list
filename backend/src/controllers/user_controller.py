from typing import Annotated
from fastapi import APIRouter, Depends, Response, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from src.forms import LoginRequestForm
from src.schemas.response import UserResponseSchema
from src.schemas.response import Token
from src.schemas.response import ErrorResponseSchema
from src.schemas.response import Token
from src.services import UserService

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@router.post('/login')
async def login(request: Annotated[LoginRequestForm, Depends()], response: Response, service: UserService = Depends()) -> Token | ErrorResponseSchema:
    token = service.login(request)

    if token:
        return token

    response.status_code = status.HTTP_401_UNAUTHORIZED

    return ErrorResponseSchema(message = 'Credenciais inválidas')

@router.get('/{user_id}')
async def getUser(user_id: int, response: Response, service: UserService = Depends()) -> UserResponseSchema | ErrorResponseSchema:
    user = service.get_user(user_id)

    if user:
        return user

    response.status_code = status.HTTP_404_NOT_FOUND

    return ErrorResponseSchema(message = 'Usuário não cadastrado')