from pydantic import BaseModel

class UpdateTodoRequestSchema(BaseModel):
    id: int
    description: str