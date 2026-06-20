from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, crud, database

router = APIRouter(prefix="/goals", tags=["goals"])

@router.post("/", response_model=schemas.GoalOut)
def create_goal(goal: schemas.GoalCreate, db: Session = Depends(database.get_db)):
    return crud.create_goal(db, goal)

@router.get("/", response_model=List[schemas.GoalOut])
def list_goals(db: Session = Depends(database.get_db)):
    return crud.get_goals(db)
