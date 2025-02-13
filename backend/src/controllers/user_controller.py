from fastapi import APIRouter, Depends, Response, status
from src.schemas.request import LoginRequestSchema
from src.schemas.response import UserResponseSchema
from src.schemas.response import ErrorResponseSchema
from src.services import UserService

router = APIRouter()

@router.post("/login")
async def login(request: LoginRequestSchema, response: Response, service: UserService = Depends()) -> UserResponseSchema | ErrorResponseSchema:
    user = service.login(request)

    if user:
        return user

    response.status_code = status.HTTP_401_UNAUTHORIZED

    return ErrorResponseSchema(message = "Invalid Credentials")
