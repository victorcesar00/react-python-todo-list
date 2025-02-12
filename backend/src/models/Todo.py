from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database import Base

class Todo(Base):
    __tablename__ = "todos"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    description: Mapped[str] = mapped_column()
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)

    owner: Mapped["User"] = relationship(back_populates="todos")