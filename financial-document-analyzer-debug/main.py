from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from crewai import Crew
from agents import pdf_agent
import tempfile
import os

app = FastAPI(title="Financial Document Analyzer")

class AnalysisRequest(BaseModel):
    query: str

@app.post("/analyze")
async def analyze_pdf(file: UploadFile = File(...), request: AnalysisRequest = None):
    try:
        # Save uploaded PDF temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(await file.read())
            tmp_path = tmp.name

        # Run CrewAI PDF agent
        result = pdf_agent.run(
            query=request.query if request else "Summarize this document",
            file_path=tmp_path
        )

        return {"status": "success", "result": result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)


@app.get("/")
async def root():
    return {"message": "Financial Document Analyzer API is running 🚀"}
