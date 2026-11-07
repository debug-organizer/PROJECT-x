from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from database import Base

class SensorReading(Base):
    __tablename__ = "sensor_readings"

    id = Column(Integer, primary_key=True, index=True)
    station_name = Column(String, index=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    rainfall_24h_mm = Column(Float)
    soil_moisture_pct = Column(Float)
    pore_pressure_kpa = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

class CitizenReport(Base):
    __tablename__ = "citizen_reports"

    id = Column(Integer, primary_key=True, index=True)
    location_name = Column(String, nullable=False)
    incident_type = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    image_path = Column(String, nullable=True)
    severity = Column(String, default="HIGH")
    status = Column(String, default="PENDING")
    timestamp = Column(DateTime, default=datetime.utcnow)

class RoadStatus(Base):
    __tablename__ = "road_status"

    id = Column(Integer, primary_key=True, index=True)
    highway_name = Column(String, index=True)
    segment_id = Column(String, nullable=False)
    status = Column(String, default="CLEAR")
    latitude_start = Column(Float)
    longitude_start = Column(Float)
    latitude_end = Column(Float)
    longitude_end = Column(Float)
    updated_at = Column(DateTime, default=datetime.utcnow)