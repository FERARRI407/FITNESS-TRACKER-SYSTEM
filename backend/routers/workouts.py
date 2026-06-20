from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, crud, database

router = APIRouter(prefix="/workouts", tags=["workouts"])

@router.post("/", response_model=schemas.WorkoutOut)
def add_workout(workout: schemas.WorkoutCreate, db: Session = Depends(database.get_db)):
    return crud.create_workout(db, workout)

@router.get("/", response_model=List[schemas.WorkoutOut])
def list_workouts(db: Session = Depends(database.get_db)):
    return crud.get_workouts(db)

@router.get("/{workout_id}", response_model=schemas.WorkoutOut)
def get_workout(workout_id: int, db: Session = Depends(database.get_db)):
    w = crud.get_workout(db, workout_id)
    if not w:
        raise HTTPException(status_code=404, detail="Workout not found")
    return w
