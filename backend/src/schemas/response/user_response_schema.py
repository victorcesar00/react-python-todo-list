from pydantic import BaseModel

class UserResponseSchema(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True