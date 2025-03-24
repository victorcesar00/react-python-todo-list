from pydantic import BaseModel, ConfigDict

class TodoResponseSchema(BaseModel):
    id: int
    description: str

    model_config = ConfigDict(
        from_attributes = True
    )