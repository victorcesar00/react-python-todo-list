from fastapi import FastAPI, Query
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

class LoginRequestSchema(BaseModel):
    username: Annotated[str, Query(min_length=5, regex="^[a-zA-Z0-9_]*$")]
    password: Annotated[str, Query(min_length=5)]