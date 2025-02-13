from pydantic import BaseModel
from typing import List
from src.schemas.response import TodoResponseSchema

class UserResponseSchema(BaseModel):
    id: int
    username: str
    todos: List[TodoResponseSchema] = []

    class Config:
        from_attributes = True