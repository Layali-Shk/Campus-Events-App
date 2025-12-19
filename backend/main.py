from fastapi import FastAPI
from database import Base, engine
from models.user import User
from models.club import Club
from models.event import Event
from models.rsvp import RSVP

# Create all database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Test route
@app.get("/")
def read_root():
    return {"message": "Campus Events API is running"}
