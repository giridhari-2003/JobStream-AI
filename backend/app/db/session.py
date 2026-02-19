from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import get_settings

settings = get_settings()
mongodb_client: AsyncIOMotorClient = None
database = None


async def connect_to_mongo():
    global mongodb_client, database

    mongodb_client = AsyncIOMotorClient(settings.MONGODB_URL)
    database = mongodb_client[settings.DATABASE_NAME]

    # Create indexes
    await create_indexes()

    print("MongoDB connected and indexes ensured.")


async def close_mongo_connection():
    mongodb_client.close()


def get_database():
    return database


async def create_indexes():
    await database.resumes.create_index("user_id")
    await database.resumes.create_index(
        [("user_id", 1), ("created_at", -1)]
    )
