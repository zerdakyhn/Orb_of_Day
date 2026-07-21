from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User

from app.schemas import (
    UserCreate,
    UserResponse,
    UserUpdate,
    ChangePassword,
    Token,
)

from app.auth import (
    hash_password,
    verify_password,
    create_access_token,
    get_current_user, 
)

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):

    # Email check
    existing_email = db.query(User).filter(User.email == user.email).first()
    if existing_email:
        raise HTTPException(
            status_code=400, 
            detail="Email already registered"
            )

    # Username check
    existing_username = db.query(User).filter(User.username == user.username).first()
    if existing_username:
        raise HTTPException(
            status_code=400, 
            detail="Username already exists"
            )

     # Hash the password
    hashed_password = hash_password(user.password)

    # Create new user
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.post("/login", response_model=Token)
def login(
  from_data: OAuth2PasswordRequestForm = Depends(),
  db: Session = Depends(get_db),
):

    # Find user by email
    db_user = db.query(User).filter(
        User.email == from_data.username
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    # Verify password
    if not verify_password(
        from_data.password,
        db_user.hashed_password 
    ):
        
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    # Create JWT token
    access_token = create_access_token(
        data={"sub": db_user.email}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@router.get("/me")
def get_me(
    current_user: str = Depends(get_current_user),
):
    return {
        "message": "Access granted",
        "email": current_user
    }
@router.put("/me", response_model=UserResponse)
def update_me(
    user_update: UserUpdate,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    # Find the authenticated user
    db_user = db.query(User).filter(
        User.email == current_user
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    # Check if the new email is already used by another user
    existing_email = db.query(User).filter(
        User.email == user_update.email,
        User.id != db_user.id
    ).first()

    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    # Check if the new username is already used by another user
    existing_username = db.query(User).filter(
        User.username == user_update.username,
        User.id != db_user.id
    ).first()

    if existing_username:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    # Update user information
    db_user.username = user_update.username
    db_user.email = user_update.email

    db.commit()
    db.refresh(db_user)

    # Return the updated user
    return db_user

@router.post("/change-password")
def change_password(
    password_data: ChangePassword,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    # Find the authenticated user
    db_user = db.query(User).filter(
        User.email == current_user
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    # Verify the current password
    if not verify_password(
        password_data.old_password,
        db_user.hashed_password
    ):
        raise HTTPException(
            status_code=400,
            detail="Current password is incorrect"
        )

    # Hash the new password
    db_user.hashed_password = hash_password(
        password_data.new_password
    )

    db.commit()

    return {
        "message": "Password updated successfully"
    }
@router.post("/logout")
def logout():
    # In a stateless JWT authentication system, logout is handled on the client side.
    # The client should simply delete the stored JWT token to "log out".
    return {
        "message": "Successfully logged out. Please remove your token from the client."
    }