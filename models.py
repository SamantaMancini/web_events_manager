from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from database import engine

# Base model definition for SQLAlchemy
Base = declarative_base()


# Model definition for the events table in the database
class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    description = Column(String(100), index=True)
    street = Column(String(100), index=True)
    date_event_start = Column(DateTime, index=True)
    date_event_end = Column(DateTime, index=True)
    timezone_event = Column(String(500), server_default='UTC0+')


Base.metadata.create_all(bind=engine)

# Pydantic model definition for creating an event (POST request)
class EventCreate(BaseModel):
    name: str = ""
    description: str = ""
    street: str = ""
    date_event_start: datetime
    date_event_end: datetime

# Pydantic model definition for updating an event (PUT request)
class EventUpdate(BaseModel):
    date_event_start: Optional[datetime] = None
    date_event_end: Optional[datetime] = None

# Pydantic model definition for displaying an event
class EventResponse(BaseModel):
    id: int
    name: str
    description: str
    street: str
    date_event_start: datetime
    date_event_end: datetime

    class Config:
        orm_mode = True