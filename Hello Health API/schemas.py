from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class PatientCreate(BaseModel):
    name: str = Field(..., example="John Doe")
    age: int = Field(..., gt=0, lt=150, example=30)
    blood_type: str = Field(..., example="A+")
    weight_kg: Optional[float] = Field(None, example=70.5)
    height_cm: Optional[float] = Field(None, example=175.0)


class PatientResponse(BaseModel):
    id: int
    name: str
    age: int
    blood_type: str
    weight_kg: Optional[float]
    height_cm: Optional[float]
    created_at: datetime
    bmi: Optional[float] = None

    class Config:
        from_attributes = True


class HealthCheck(BaseModel):
    status: str
    message: str
    version: str
