from pydantic import BaseModel

class UpdateTodoRequest(BaseModel):
    id: int
    description: str