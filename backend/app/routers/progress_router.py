from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Progress
from ..schemas import ProgressCreate

router = APIRouter(tags=["Progress"])


@router.post("/progress")
def add_progress(progress: ProgressCreate,
                 db: Session = Depends(get_db)):

    new_progress = Progress(**progress.dict())

    db.add(new_progress)
    db.commit()

    return new_progress


@router.get("/progress")
def get_progress(db: Session = Depends(get_db)):
    return db.query(Progress).all()