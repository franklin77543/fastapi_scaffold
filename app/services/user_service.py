from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserUpdate, UserResponse


class UserService:
    def __init__(self, db: Session):
        self.user_repo = UserRepository(db)

    def create_user(self, user: UserCreate) -> UserResponse:
        db_user = self.user_repo.create(user)
        return UserResponse.from_orm(db_user)

    def get_user_by_id(self, user_id: int) -> UserResponse | None:
        db_user = self.user_repo.get_by_id(user_id)
        if not db_user:
            return None
        return UserResponse.from_orm(db_user)

    def get_user_by_username(self, username: str) -> UserResponse | None:
        db_user = self.user_repo.get_by_username(username)
        if not db_user:
            return None
        return UserResponse.from_orm(db_user)

    def get_all_users(self, skip: int = 0, limit: int = 100) -> list[UserResponse]:
        users = self.user_repo.get_all(skip, limit)
        return [UserResponse.from_orm(u) for u in users]

    def update_user(self, user_id: int, user: UserUpdate) -> UserResponse | None:
        db_user = self.user_repo.update(user_id, user)
        if not db_user:
            return None
        return UserResponse.from_orm(db_user)

    def delete_user(self, user_id: int) -> bool:
        return self.user_repo.delete(user_id)
