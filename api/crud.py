from datetime import datetime, timedelta
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
    hashed_password = hashlib.sha256(user.password.encode()).hexdigest()
    db_user = models.User(email=user.email, hashed_password=hashed_password, firstname=user.firstname, lastname=user.lastname, is_active = user.is_active)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def activate_user(db: Session, email:str):
    db_user = get_user_by_email(db, email)
    db_user.is_active = True
    db.add(db_user)
    db.commit()
    db.refresh(db_user)


def get_token(db: Session, token: str):
    return db.query(models.Token).filter(models.Token.token == token).first()


def remove_token(db: Session, token: str):
    todo = db.query(models.Token).filter(models.Token.token== token).first() # Todo object
    db.delete(todo)
    db.commit()

def create_token(db: Session, token: str, email):
    expiry = datetime.now() + timedelta(hours = 24)
    db_token = models.Token(token = token, email = email, expiry = expiry )
    db.add(db_token)
    db.commit()

    return db.query(models.User).filter(models.Token.token == token).first()

def create_activateKey(db: Session, key: str, email):
    expiry = datetime.now() + timedelta(hours = 1)
    db_activateUser = models.ActivateUser(verify_key = key, email = email, expiry = expiry)
    db.add(db_activateUser)
    db.commit()


def get_activateKey(db: Session, key):
    return db.query(models.ActivateUser).filter(models.ActivateUser.verify_key == key).first()


def remove_activateKey(db: Session, key):
    todo = db.query(models.ActivateUser).filter(models.ActivateUser.verify_key== key).first() # Todo object
    db.delete(todo)
    db.commit()
