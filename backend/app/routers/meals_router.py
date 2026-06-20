from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Meal
from ..schemas import MealCreate

router = APIRouter(tags=["Meals"])


@router.post("/meals")
def create_meal(meal: MealCreate,
                db: Session = Depends(get_db)):

    new_meal = Meal(**meal.dict())

    db.add(new_meal)
    db.commit()

    return new_meal


@router.get("/meals")
def get_meals(db: Session = Depends(get_db)):
    return db.query(Meal).all()