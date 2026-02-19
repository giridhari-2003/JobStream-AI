from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from bson import ObjectId

from app.core.dependencies import get_current_user
from app.db.session import get_database
from app.db.repositories.resume_repository import ResumeRepository
from app.services.resume_service import ResumeService
from app.schemas.resume import ResumeResponse

router = APIRouter(prefix="/resume", tags=["Resume"])


# ---------------------------
# Upload Resume
# ---------------------------
@router.post("/upload")
async def upload_resume(
    file: UploadFile = File(...),
    current_user=Depends(get_current_user)
):
    db = get_database()
    repo = ResumeRepository(db)
    service = ResumeService(repo)

    resume_id, structured = await service.upload_resume(
        current_user["id"], file
    )

    return {
        "message": "Resume uploaded successfully",
        "resume_id": resume_id,
        "skills_detected": len(structured["skills"])
    }


# ---------------------------
# Get Latest Resume
# ---------------------------
@router.get("/")
async def get_my_resume(current_user=Depends(get_current_user)):

    db = get_database()
    repo = ResumeRepository(db)

    resume = await repo.get_latest_by_user(current_user["id"])

    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")

    return {
        "resume_id": str(resume["_id"]),
        "file_path": resume["file_path"],
        "skills": resume["structured_data"].get("skills", []),
        "projects": resume["structured_data"].get("projects", []),
        "experience_summary": resume["structured_data"].get("experience_summary"),
        "uploaded_at": resume["created_at"]
    }


# ---------------------------
# Get Resume By ID
# ---------------------------
@router.get("/{resume_id}")
async def get_resume_by_id(
    resume_id: str,
    current_user=Depends(get_current_user)
):
    db = get_database()
    repo = ResumeRepository(db)

    resume = await repo.get_by_id(resume_id)

    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")

    if str(resume["user_id"]) != current_user["id"]:
        raise HTTPException(status_code=403, detail="Unauthorized")

    return {
        "resume_id": str(resume["_id"]),
        "file_path": resume["file_path"],
        "skills": resume["structured_data"].get("skills", []),
        "projects": resume["structured_data"].get("projects", []),
        "experience_summary": resume["structured_data"].get("experience_summary"),
        "uploaded_at": resume["created_at"]
    }


# ---------------------------
# Delete Resume
# ---------------------------
@router.delete("/{resume_id}")
async def delete_resume(
    resume_id: str,
    current_user=Depends(get_current_user)
):
    db = get_database()
    repo = ResumeRepository(db)

    resume = await repo.get_by_id(resume_id)

    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")

    if str(resume["user_id"]) != current_user["id"]:
        raise HTTPException(status_code=403, detail="Unauthorized")

    await repo.delete_resume(resume_id)

    return {"message": "Resume deleted successfully"}


# ---------------------------
# Reprocess Resume
# ---------------------------
@router.post("/{resume_id}/reprocess")
async def reprocess_resume(
    resume_id: str,
    current_user=Depends(get_current_user)
):
    db = get_database()
    repo = ResumeRepository(db)
    service = ResumeService(repo)

    resume = await repo.get_by_id(resume_id)

    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")

    if str(resume["user_id"]) != current_user["id"]:
        raise HTTPException(status_code=403, detail="Unauthorized")

    structured = service.basic_parse(resume["extracted_text"])

    await repo.update_resume(resume_id, {
        "structured_data": structured
    })

    return {
        "message": "Resume reprocessed successfully",
        "skills_detected": len(structured["skills"])
    }
