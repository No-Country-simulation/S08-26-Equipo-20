from fastapi import FastAPI

from app.routers.auth import router as auth_router

app = FastAPI(title="ServiceFlowAPI")

app.include_router(auth_router, prefix="/api")


@app.get("/api/health")

def health_check():
    return {"status": "ok"}
