from bson import ObjectId
from datetime import datetime

class ResumeRepository:

    def __init__(self, db):
        self.collection = db.resumes

    async def create_resume(self, data: dict):
        data["created_at"] = datetime.utcnow()
        result = await self.collection.insert_one(data)
        return str(result.inserted_id)

    async def get_latest_by_user(self, user_id: str):
        return await self.collection.find_one(
            {"user_id": ObjectId(user_id)},
            sort=[("created_at", -1)]
        )

    async def get_by_id(self, resume_id: str):
        return await self.collection.find_one(
            {"_id": ObjectId(resume_id)}
        )

    async def delete_resume(self, resume_id: str):
        return await self.collection.delete_one(
            {"_id": ObjectId(resume_id)}
        )

    async def update_resume(self, resume_id: str, data: dict):
        return await self.collection.update_one(
            {"_id": ObjectId(resume_id)},
            {"$set": data}
        )
