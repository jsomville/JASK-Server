
from sqlalchemy.orm import Session

from . import crud, schemas

def init_data(db: Session):
    password = "1234"
    
    u = schemas.UserCreate(email="john.dow@email.com", firstname="John", lastname="Dow", password=password, is_active=True)
    crud.create_user(db, u)

    u = schemas.UserCreate(email="jane.dow@email.com", firstname="Jane", lastname="Dow", password=password, is_active=True)
    crud.create_user(db, u)

    u = schemas.UserCreate(email="jr.dow@email.com", firstname="Jr.", lastname="Dow", password=password, is_active=True)
    crud.create_user(db, u)

    