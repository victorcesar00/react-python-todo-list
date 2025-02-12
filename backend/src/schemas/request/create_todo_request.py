from pydantic import BaseModel

class CreateTodoRequest(BaseModel):
    user_id: int
    description: str