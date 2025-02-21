from fastapi import FastAPI, HTTPException, Form
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from pydantic import ValidationError
from src.schemas.request import LoginRequestSchema

app = FastAPI()

class LoginRequestForm(OAuth2PasswordRequestForm):
    def __init__(self, username: str = Form(...), password: str = Form(...)):
        self._validate_credentials(username, password)

        super().__init__(username=username, password=password)

    @staticmethod
    def _validate_credentials(username: str, password: str) -> None:
        try:
            LoginRequestSchema(username=username, password=password)
        except ValidationError as e:
            raise HTTPException(status_code=422, detail=e.errors())