from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routers.auth import router as auth_router

app = FastAPI(title="ServiceFlowAPI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in settings.ALLOWED_ORIGINS.split(",")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/api")


@app.get("/api/health")

def health_check():
    return {"status": "ok"}
