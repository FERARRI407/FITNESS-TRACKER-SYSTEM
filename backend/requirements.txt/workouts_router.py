from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Workout
from schemas import WorkoutCreate

router = APIRouter(tags=["Workouts"])


@router.post("/workouts")
def create_workout(workout: WorkoutCreate,
                   db: Session = Depends(get_db)):

    new_workout = Workout(**workout.dict())

    db.add(new_workout)
    db.commit()

    return new_workout


@router.get("/workouts")
def get_workouts(db: Session = Depends(get_db)):
    return db.query(Workout).all()


@router.delete("/workouts/{id}")
def delete_workout(id: int,
                   db: Session = Depends(get_db)):

    workout = db.query(Workout).filter(
        Workout.workout_id == id
    ).first()

    db.delete(workout)
    db.commit()

    return {"message": "Workout deleted"}