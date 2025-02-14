from pydantic import BaseModel

class TodoResponseSchema(BaseModel):
    id: int
    description: str

    class Config:
        from_attributes = True