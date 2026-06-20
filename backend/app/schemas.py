from pydantic import BaseModel
from datetime import date


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class WorkoutCreate(BaseModel):
    user_id: int
    workout_type: str
    duration: int
    calories_burned: float
    workout_date: date


class GoalCreate(BaseModel):
    user_id: int
    target_weight: float
    target_calories: float


class ProgressCreate(BaseModel):
    user_id: int
    current_weight: float
    bmi: float
    date_recorded: date


class MealCreate(BaseModel):
    user_id: int
    meal_name: str
    calories: float