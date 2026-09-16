from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine

from app.models.building import Building
from app.models.finding import AuditFinding
from app.models.issue import Issue
from app.models.evidence import Evidence
from app.models.finding_evidence import FindingEvidence
from app.models.complaint import Complaint
from app.models.authority_response import AuthorityResponse

from app.routes.buildings import router as buildings_router
from app.routes.audits import router as audits_router
from app.routes.findings import router as findings_router
from app.routes.issues import router as issues_router
from app.routes.analysis import router as analysis_router
from app.routes.evidence import router as evidence_router
from app.routes.measurements import router as measurements_router
from app.routes.standards import router as standards_router
from app.routes.complaints import router as complaints_router
from app.routes.authority_responses import (
    router as authority_responses_router
)
from app.models.corrective_action import CorrectiveAction
from app.routes.corrective_actions import (
    router as corrective_actions_router
)
# ============================================================
# DATABASE
# ============================================================

Base.metadata.create_all(bind=engine)


# ============================================================
# FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="Accessibility Accountability Platform",
    description=(
        "Open-source accessibility audit "
        "and accountability platform"
    ),
    version="0.1.0",
)


# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174",
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


# ============================================================
# ROUTERS
# ============================================================

app.include_router(buildings_router)

app.include_router(audits_router)

app.include_router(findings_router)

app.include_router(issues_router)

app.include_router(analysis_router)

app.include_router(evidence_router)

app.include_router(measurements_router)

app.include_router(standards_router)

app.include_router(complaints_router)

app.include_router(
    authority_responses_router
)
app.include_router(
    corrective_actions_router
)

# ============================================================
# ROOT
# ============================================================

@app.get("/")
def root():

    return {
        "message": (
            "Accessibility Accountability "
            "Platform API"
        ),
        "status": "running",
    }


# ============================================================
# HEALTH
# ============================================================

@app.get("/health")
def health():

    return {
        "status": "healthy",
    }


# ============================================================
# DATABASE HEALTH
# ============================================================

@app.get("/health/database")
def database_health():

    try:

        with engine.connect():

            return {
                "database": "connected",
            }

    except Exception as e:

        return {
            "database": "error",
            "message": str(e),
        }