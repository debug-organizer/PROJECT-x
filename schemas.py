from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SensorReadingCreate(BaseModel):
    station_name: str
    latitude: float
    longitude: float
    rainfall_24h_mm: float
    soil_moisture_pct: float
    pore_pressure_kpa: float

class SensorReadingResponse(SensorReadingCreate):
    id: int
    timestamp: datetime
    class Config:
        from_attributes = True

class CitizenReportResponse(BaseModel):
    id: int
    location_name: str
    incident_type: str
    description: Optional[str]
    latitude: float
    longitude: float
    image_path: Optional[str]
    severity: str
    status: str
    timestamp: datetime
    class Config:
        from_attributes = True

class RiskPredictionRequest(BaseModel):
    rainfall_24h_mm: float
    soil_moisture_pct: float
    slope_angle_deg: float

class BroadcastRequest(BaseModel):
    message: Optional[str] = ""
    language: str = "en"
    district: str