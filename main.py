from typing import List
from pytest import Session
from database import get_db

from fastapi import Depends, FastAPI
from datetime import datetime
from models import EventCreate, EventUpdate
from controllers import create_Event, delete_event, read_event, read_events, update_event
from models import EventResponse

# Initialize the FastAPI application
app = FastAPI()


# Controller for creating a new event (POST)
@app.post("/events/", response_model=EventResponse, status_code=201)
def create_event_end_point(event: EventCreate, db: Session = Depends(get_db)):
    return create_Event(event, db)
# Controller for reading all events (GET) with pagination
@app.get("/events/", response_model=List[EventResponse], status_code=200)
def read_events_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return read_events(skip, limit, db)
# Controller for searching events on a specific date (GET)
@app.get("/events/{event_id}", response_model=List[EventResponse], status_code=200)
def read_event_endpoint(event_id: datetime, db: Session = Depends(get_db)):
    return read_event(event_id, db)
# Controller for updating an existing event (PUT)
@app.put("/events/{event_id}", response_model=EventResponse, status_code=200)
def update_event_endpoint(event_id: int, event: EventUpdate, db: Session = Depends(get_db)):
    return update_event(event_id, event, db)
# Controller for deleting an event (DELETE)
@app.delete("/events/{event_id}", response_model=EventResponse, status_code=202)
def delete_event_endpoint(event_id: int, db: Session = Depends(get_db)):
    return delete_event(event_id, db)