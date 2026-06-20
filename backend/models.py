from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base
import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    age = Column(Integer)
    weight = Column(Float)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    workouts = relationship("Workout", back_populates="owner")
    goals = relationship("Goal", back_populates="owner")

class Workout(Base):
    __tablename__ = "workouts"
    workout_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    workout_type = Column(String, nullable=False)
    duration_minutes = Column(Integer)
    calories_burned = Column(Integer)
    workout_date = Column(Date)

    owner = relationship("User", back_populates="workouts")

class Goal(Base):
    __tablename__ = "goals"
    goal_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    goal_name = Column(String, nullable=False)
    target_value = Column(Integer)
    current_progress = Column(Integer, default=0)
    deadline = Column(Date)

    owner = relationship("User", back_populates="goals")
