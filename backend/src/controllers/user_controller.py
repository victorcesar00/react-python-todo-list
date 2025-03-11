from typing import Annotated
from fastapi import APIRouter, Depends, Response, status
from fastapi.security import OAuth2PasswordBearer
from src.forms import LoginRequestForm
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

    return ErrorResponseSchema(message = 'Invalid credentials')

@router.get('/validate-token')
async def validate_token() -> bool:
    return True