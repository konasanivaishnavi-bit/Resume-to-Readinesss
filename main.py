"""Optional API starter for Resume to Readiness.
Run: uvicorn main:app --reload
Keep API keys on the server; never put them in app.js or a public frontend.
"""
from __future__ import annotations
import os
from typing import Any
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI(title="Resume to Readiness API", version="0.1.0")
allowed = os.getenv("FRONTEND_ORIGIN", "http://localhost:5500")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[allowed, "http://127.0.0.1:5500", "http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

class AnalyzeRequest(BaseModel):
    resume_text: str = Field(min_length=30, max_length=50000)
    job_description: str = Field(min_length=20, max_length=20000)
    target_role: str = Field(default="Target role", max_length=100)

class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=2000)
    context: dict[str, Any] = Field(default_factory=dict)

SKILL_TERMS = {
    "Python": ["python", "pandas", "flask", "fastapi", "django"],
    "Data Structures & Algorithms": ["data structures", "algorithms", "leetcode", "dsa", "binary search"],
    "SQL / DBMS": ["sql", "postgresql", "mysql", "database", "dbms", "joins", "normalization"],
    "Git & GitHub": ["git", "github", "version control", "pull request"],
    "REST APIs": ["rest api", "fastapi", "flask", "endpoint", "api development"],
    "Projects & Evidence": ["project", "deployed", "portfolio", "built", "developed", "implemented"],
    "Communication": ["presentation", "documentation", "team", "collaborated"],
}
ACTIONS = {
    "Python": "Build a small Python API with input validation and tests.",
    "Data Structures & Algorithms": "Solve and explain five beginner problems; include time complexity.",
    "SQL / DBMS": "Practice joins, grouping, indexes, and normalization.",
    "Git & GitHub": "Create a clean repository with a README and meaningful commits.",
    "REST APIs": "Build and document a CRUD endpoint with error handling.",
    "Projects & Evidence": "Add a project with problem, approach, technology, and genuine outcomes.",
    "Communication": "Practice a 90-second explanation of one project.",
}

@app.get("/health")
def health():
    return {"status": "ok", "service": "resume-to-readiness-api"}

@app.post("/analyze")
def analyze(req: AnalyzeRequest):
    resume = req.resume_text.casefold()
    jd = req.job_description.casefold()
    skills = []
    for name, terms in SKILL_TERMS.items():
        if not any(t in jd for t in terms) and len(jd) >= 20:
            continue
        hits = [t for t in terms if t in resume]
        status = "match" if len(hits) >= 2 else "partial" if hits else "gap"
        evidence = f"Found related wording: {', '.join(hits[:3])}." if hits else "No clear keyword evidence found in extracted resume text."
        skills.append({"name": name, "status": status, "evidence": evidence, "action": ACTIONS[name]})
    if not skills:
        skills = [{"name": n, "status": "partial" if any(t in resume for t in terms) else "gap",
                   "evidence": "Compared against the initial skill dictionary.", "action": ACTIONS[n]}
                  for n, terms in list(SKILL_TERMS.items())[:5]]
    points = sum(1 if s["status"] == "match" else .5 if s["status"] == "partial" else 0 for s in skills)
    score = round(points / len(skills) * 100)
    gaps = [s for s in skills if s["status"] != "match"]
    return {
        "target_role": req.target_role,
        "score": score,
        "matched_or_partial": len([s for s in skills if s["status"] != "gap"]),
        "skills": skills,
        "next_step": (f"Start with {gaps[0]['name']}: {gaps[0]['action']}" if gaps
                      else "Strengthen project evidence with real outcomes and practice explaining trade-offs."),
        "method": "transparent_keyword_baseline",
        "limitation": "This is an illustrative keyword baseline, not validated semantic AI or a hiring prediction."
    }

@app.post("/bixby")
def bixby(req: ChatRequest):
    """A safe demo response. Add a server-side LLM provider here when credentials are configured."""
    if not os.getenv("LLM_API_KEY"):
        return {
            "reply": "I'm Bixby in demo mode. I can help you plan a study week, explain your readiness report, or practice an interview. A live LLM has not been configured yet.",
            "mode": "demo",
            "next_setup": "Set LLM_API_KEY on the server and implement your chosen provider call here."
        }
    # Deliberately do not send data to an unspecified provider. Implement the approved LLM provider call here.
    raise HTTPException(status_code=501, detail="LLM_API_KEY exists, but no provider adapter has been configured. Add the selected LLM SDK and server-side request here.")
