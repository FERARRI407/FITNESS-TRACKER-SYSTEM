from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Goal
from ..schemas import GoalCreate

router = APIRouter(tags=["Goals"])


@router.post("/goals")
def create_goal(goal: GoalCreate,
                db: Session = Depends(get_db)):

    new_goal = Goal(**goal.dict())

    db.add(new_goal)
    db.commit()

    return new_goal


@router.get("/goals")
def get_goals(db: Session = Depends(get_db)):
    return db.query(Goal).all()