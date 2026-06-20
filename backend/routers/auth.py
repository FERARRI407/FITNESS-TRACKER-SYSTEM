from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models, crud, database
from passlib.context import CryptContext
import os, jwt, datetime

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = os.getenv("SECRET_KEY", "change-me")
ALGORITHM = "HS256"

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    if crud.get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed = pwd_context.hash(user.password)
    return crud.create_user(db, user, hashed)

@router.post("/login")
def login(form: schemas.Login, db: Session = Depends(database.get_db)):
    user = crud.get_user_by_email(db, form.email)
    if not user or not pwd_context.verify(form.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    payload = {"sub": str(user.id), "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=8)}
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}
