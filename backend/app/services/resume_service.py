import os
import uuid
import fitz  # PyMuPDF
from bson import ObjectId

class ResumeService:

    def __init__(self, repo):
        self.repo = repo

    async def upload_resume(self, user_id: str, file):

        file_ext = file.filename.split(".")[-1]
        if file_ext.lower() != "pdf":
            raise Exception("Only PDF allowed")

        filename = f"{uuid.uuid4()}.pdf"
        file_path = f"media/resumes/{filename}"

        os.makedirs("media/resumes", exist_ok=True)

        with open(file_path, "wb") as f:
            f.write(await file.read())

        extracted_text = self.extract_text(file_path)
        structured = self.basic_parse(extracted_text)

        resume_id = await self.repo.create_resume({
            "user_id": ObjectId(user_id),
            "file_path": file_path,
            "extracted_text": extracted_text,
            "structured_data": structured
        })

        return resume_id, structured

    def extract_text(self, path):
        doc = fitz.open(path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text

    def basic_parse(self, text):
        # Replace later with LLM
        skills = []
        keywords = ["Python", "FastAPI", "MongoDB", "YOLO", "LangChain"]

        for k in keywords:
            if k.lower() in text.lower():
                skills.append(k)

        return {
            "skills": skills,
            "projects": [],
            "experience_summary": text[:500]
        }
