from fastapi import APIRouter, Depends, Response, status
from src.schemas.request import LoginRequest
from src.schemas.response import UserResponse
from src.schemas.response import ErrorResponse
from src.services import UserService

router = APIRouter()

@router.post("/login")
async def login(request: LoginRequest, response: Response, service: UserService = Depends()) -> UserResponse | ErrorResponse:
    user = service.login(request)

    if user:
        return user

    response.status_code = status.HTTP_401_UNAUTHORIZED

    return ErrorResponse(message = "Invalid Credentials")
