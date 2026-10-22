from fastapi import FastAPI, HTTPException

from backend.generator import generate_excuse
from backend.schemas import ExcuseRequest, ExcuseResponse, HealthResponse

app = FastAPI(title="Excuse Generator API")

@app.get("/health", response_model=HealthResponse)
def health_check():
    return {"status": "healthy", "version": "1.0.0"}

@app.post("/generate", response_model=ExcuseResponse)
def generate(request: ExcuseRequest):
    if not request.situation:
        raise HTTPException(status_code=400, detail="Situation is required")

    result = generate_excuse(
        situation=request.situation,
        absurdity_level=request.absurdity_level,
        include_moon_phase=request.include_moon_phase
    )
    return {"status": "success", "data": result}