from pydantic import BaseModel, EmailStr
from typing import Optional
import datetime

class UserBase(BaseModel):
    name: str
    email: EmailStr
    age: Optional[int] = None
    weight: Optional[float] = None

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    created_at: datetime.datetime
    class Config:
        orm_mode = True

class Login(BaseModel):
    email: EmailStr
    password: str

class WorkoutBase(BaseModel):
    workout_type: str
    duration_minutes: int
    calories_burned: int
    workout_date: datetime.date

class WorkoutCreate(WorkoutBase):
    user_id: int

class WorkoutOut(WorkoutBase):
    workout_id: int
    class Config:
        orm_mode = True

class GoalBase(BaseModel):
    goal_name: str
    target_value: int
    deadline: datetime.date

class GoalCreate(GoalBase):
    user_id: int

class GoalOut(GoalBase):
    goal_id: int
    current_progress: int
    class Config:
        orm_mode = True
