from datetime import datetime
from bson import ObjectId
from fastapi import HTTPException, status
from app.db.session import get_database
from app.core.security import hash_password, verify_password, create_access_token


class AuthService:

    @staticmethod
    async def register(data):
        db = get_database()

        existing = await db.users.find_one({"email": data.email})
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered",
            )

        user_doc = {
            "email": data.email,
            "hashed_password": hash_password(data.password),
            "full_name": data.full_name,
            "is_active": True,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow(),
        }

        result = await db.users.insert_one(user_doc)

        return {"message": "User registered successfully"}

    @staticmethod
    async def login(data):
        db = get_database()

        user = await db.users.find_one({"email": data.email})
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
            )

        if not verify_password(data.password, user["hashed_password"]):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
            )

        token = create_access_token({"sub": str(user["_id"])})

        return {
            "access_token": token,
            "token_type": "bearer",
        }
