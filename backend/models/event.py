from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from database import Base

class Event(Base):
    __tablename__="events"

    id=Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    descrition = Column(String)
    date = Column(DateTime, nullable=False)
    club_id = Column(Integer, ForeignKey("clubs.id"))