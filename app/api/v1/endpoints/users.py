from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.user import UserCreate, UserUpdate, UserResponse
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    existing_user = service.get_user_by_username(user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    return service.create_user(user)


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    user = service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("", response_model=list[UserResponse])
def get_all_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.get_all_users(skip, limit)


@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    service = UserService(db)
    updated_user = service.update_user(user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    success = service.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return None
