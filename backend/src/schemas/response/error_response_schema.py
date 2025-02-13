from pydantic import BaseModel

class ErrorResponseSchema(BaseModel):
    message: str