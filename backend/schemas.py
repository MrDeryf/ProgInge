from pydantic import BaseModel


class ExcuseRequest(BaseModel):
    situation: str
    absurdity_level: int = 5
    include_moon_phase: bool = False

class ExcuseData(BaseModel):
    excuse: str
    factors_used: list[str]
    calculated_score: float

class ExcuseResponse(BaseModel):
    status: str
    data: ExcuseData

class HealthResponse(BaseModel):
    status: str
    version: str