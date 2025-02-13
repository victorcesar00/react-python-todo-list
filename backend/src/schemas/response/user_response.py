from pydantic import BaseModel
from typing import List
from src.schemas.response import TodoResponse

class UserResponse(BaseModel):
    id: int
    username: str
    todos: List[TodoResponse] = []

    class Config:
        from_attributes = True