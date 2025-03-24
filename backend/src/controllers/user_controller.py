from typing import Annotated, Union
from fastapi import APIRouter, Depends, Request, Response, status
from fastapi.security import OAuth2PasswordBearer
from src.forms import LoginRequestForm
from src.schemas.response import ErrorResponseSchema
from src.schemas.response import Token
from src.services.interfaces import UserServiceInterface
from src.services import UserService
from src.limiter import limiter

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@router.post('/login', response_model=Union[Token, ErrorResponseSchema])
@limiter.limit('1/second')
async def login(login_form: Annotated[LoginRequestForm, Depends()], request: Request, response: Response, service: UserServiceInterface = Depends(UserService)):
    token = service.login(login_form)

    if token:
        return token

    response.status_code = status.HTTP_401_UNAUTHORIZED

    return ErrorResponseSchema(message = 'Invalid credentials')

@router.get('/validate-token', response_model=bool)
@limiter.limit('5/second')
async def validate_token(request: Request):
    return True