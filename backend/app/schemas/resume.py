from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ResumeResponse(BaseModel):
    resume_id: str
    file_url: str
    skills: List[str]
    projects: List[str]
    experience_summary: Optional[str]
    uploaded_at: datetime


class ResumeUploadResponse(BaseModel):
    message: str
    resume_id: str
    skills_detected: int
