from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    location = Column(String, nullable=False)
    creator_id = Column(Integer, ForeignKey("users.id"))

if __name__ == "__main__":
    from database import engine
    Base.metadata.create_all(bind=engine)
    print("Database tables created!")
