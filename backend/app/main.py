from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.session import connect_to_mongo, close_mongo_connection
from app.core.config import get_settings
from app.api.v1.auth.router import router as auth_router
from app.api.v1.resume.router import router as resume_router

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_to_mongo()
    yield
    await close_mongo_connection()


app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(auth_router, prefix=settings.API_V1_STR)
app.include_router(resume_router, prefix=settings.API_V1_STR)
