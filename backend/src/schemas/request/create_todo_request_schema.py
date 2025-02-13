from pydantic import BaseModel

class CreateTodoRequestSchema(BaseModel):
    user_id: int
    description: str