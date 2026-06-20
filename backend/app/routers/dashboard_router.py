from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import User, Workout, Goal, Progress, Meal

router = APIRouter(tags=["Dashboard"])


@router.get("/dashboard")
def dashboard(db: Session = Depends(get_db)):

    users = db.query(User).count()
    workouts = db.query(Workout).count()
    goals = db.query(Goal).count()
    progress = db.query(Progress).count()
    meals = db.query(Meal).count()

    return {
        "users": users,
        "workouts": workouts,
        "goals": goals,
        "progress": progress,
        "meals": meals
    }