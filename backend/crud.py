from sqlalchemy.orm import Session
from . import models, schemas

# Users
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate, hashed_password: str):
    db_user = models.User(name=user.name, email=user.email, password=hashed_password, age=user.age, weight=user.weight)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Workouts
def create_workout(db: Session, workout: schemas.WorkoutCreate):
    db_w = models.Workout(**workout.dict())
    db.add(db_w)
    db.commit()
    db.refresh(db_w)
    return db_w

def get_workouts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Workout).offset(skip).limit(limit).all()

def get_workout(db: Session, workout_id: int):
    return db.query(models.Workout).filter(models.Workout.workout_id == workout_id).first()

# Goals
def create_goal(db: Session, goal: schemas.GoalCreate):
    db_g = models.Goal(**goal.dict())
    db.add(db_g)
    db.commit()
    db.refresh(db_g)
    return db_g

def get_goals(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Goal).offset(skip).limit(limit).all()
