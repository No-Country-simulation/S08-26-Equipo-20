from fastapi import FastAPI

app = FastAPI(title="ServiceFlowAPI")

@app.get("/api/health")

def health_check():
    return {"status": "ok"}
