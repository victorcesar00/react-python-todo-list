from pydantic import BaseModel

class TodoResponse(BaseModel):
    id: int
    description: str
    user_id: int

    class Config:
        from_attributes = True