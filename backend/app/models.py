from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy import ForeignKey
from .database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String, unique=True)
    password = Column(String)


class Workout(Base):
    __tablename__ = "workouts"

    workout_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    workout_type = Column(String)
    duration = Column(Integer)
    calories_burned = Column(Float)
    workout_date = Column(Date)


class Goal(Base):
    __tablename__ = "goals"

    goal_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    target_weight = Column(Float)
    target_calories = Column(Float)


class Progress(Base):
    __tablename__ = "progress"

    progress_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    current_weight = Column(Float)
    bmi = Column(Float)
    date_recorded = Column(Date)


class Meal(Base):
    __tablename__ = "meals"

    meal_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    meal_name = Column(String)
    calories = Column(Float)