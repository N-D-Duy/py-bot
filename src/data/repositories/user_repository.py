from sqlalchemy.orm import Session
from src.data.schemas.user import User
from typing import Optional, Type


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, user_id: int) -> Optional[User]:
        return self.db.query(User).filter(User.id == user_id).first()

    def get_by_platform_id(self, platform_id: str) -> Optional[User]:
        return self.db.query(User).filter(User.platform_id == platform_id).first()

    def get_all_active(self) -> list[Type[User]]:
        return self.db.query(User).filter(User.is_active == True).all()

    def create(self, platform_id: str, username: str, first_name: str = None, last_name: str = None) -> User:
        user = User(
            platform_id=platform_id,
            username=username,
            first_name=first_name,
            last_name=last_name
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def update(self, user: User) -> User:
        self.db.commit()
        self.db.refresh(user)
        return user

    def deactivate(self, user_id: int) -> bool:
        user = self.get_by_id(user_id)
        if user:
            user.is_active = False
            self.db.commit()
            return True
        return False