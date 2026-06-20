from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database, models

router = APIRouter(prefix="/dashboard", tags=["dashboard"])

@router.get("/stats")
def stats(db: Session = Depends(database.get_db)):
    users = db.query(models.User).count()
    workouts = db.query(models.Workout).count()
    goals = db.query(models.Goal).count()
    return {"users": users, "workouts": workouts, "goals": goals}
