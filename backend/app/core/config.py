from pydantic_settings import BaseSettings
from typing import Literal


class Settings(BaseSettings):
    # ----------------------------
    # Core Project Config
    # ----------------------------
    PROJECT_NAME: str = "JobStream AI"
    API_V1_STR: str = "/api/v1"

    # ----------------------------
    # MongoDB
    # ----------------------------
    MONGODB_URL: str
    DATABASE_NAME: str = "jobstream_ai"

    # ----------------------------
    # Security / JWT
    # ----------------------------
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24

    # ----------------------------
    # Resume Storage
    # ----------------------------
    STORAGE_TYPE: Literal["local", "s3"] = "local"

    MEDIA_ROOT: str = "media"
    RESUME_FOLDER: str = "media/resumes"
    MAX_RESUME_SIZE_MB: int = 5

    # ----------------------------
    # AWS S3 (Optional - future ready)
    # ----------------------------
    AWS_ACCESS_KEY_ID: str | None = None
    AWS_SECRET_ACCESS_KEY: str | None = None
    AWS_BUCKET_NAME: str | None = None
    AWS_REGION: str | None = None

    # ----------------------------
    # LLM (Optional - for advanced resume parsing later)
    # ----------------------------
    LLM_PROVIDER: str | None = None
    OPENAI_API_KEY: str | None = None

    class Config:
        env_file = ".env"
        case_sensitive = True


def get_settings():
    return Settings()
