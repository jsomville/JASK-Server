from sqlalchemy.orm import Session

from api import schemas, models

import hashlib

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_email_and_hashed_password(db: Session, email: str, hashed_password : str):
    return db.query(models.User).filter(models.User.email == email, models.User.hashed_password == hashed_password).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = hashed_Password = hashlib.sha256(user.password.encode()).hexdigest()
    db_user = models.User(email=user.email, hashed_password=hashed_password, firstname=user.firstname, lastname=user.lastname)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
