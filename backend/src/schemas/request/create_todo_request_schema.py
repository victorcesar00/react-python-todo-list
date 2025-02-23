from pydantic import BaseModel

class CreateTodoRequestSchema(BaseModel):
    description: str