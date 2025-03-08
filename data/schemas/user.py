from sqlalchemy import Column, Integer, String, DateTime, Boolean, func
from data.database.base import Base
from pydantic import BaseModel


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    platform_id = Column(String(255), unique=True, index=True, nullable=False)
    username = Column(String(255))
    first_name = Column(String(255))
    last_name = Column(String(255))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


    def __repr__(self):
        return f"<User {self.username}>"


class UserCreate(BaseModel):
    platform_id: str
    username: str = None
    first_name: str = None
    last_name: str = None
    is_active: bool = True