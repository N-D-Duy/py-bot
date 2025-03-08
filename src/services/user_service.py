from sqlalchemy.orm import Session
from src.data.repositories.user_repository import UserRepository
from src.data.database.session import get_db

class UserService:
    def __init__(self, db: Session = None):
        self.db = db or next(get_db())
        self.user_repository = UserRepository(self.db)

    def get_or_create_user(self, platform_id, username, first_name=None, last_name=None):
        user = self.user_repository.get_by_platform_id(platform_id)
        if not user:
            user = self.user_repository.create(
                platform_id=platform_id,
                username=username,
                first_name=first_name,
                last_name=last_name
            )
        return user

    def get_all_active_users(self):
        return self.user_repository.get_all_active()