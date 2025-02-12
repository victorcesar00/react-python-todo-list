from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database import Base

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    username: Mapped[str] = mapped_column(unique=True, index=True)
    password: Mapped[str] = mapped_column()

    todos: Mapped[List["Todo"]] = relationship(back_populates="owner")