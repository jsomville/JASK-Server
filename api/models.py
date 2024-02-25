from click import DateTime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, func, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    firstname = Column(String)
    lastname = Column(String)

class Token(Base):
    __tablename__ = "token"

    token=Column(String, primary_key=True)
    email = Column(String, unique=True)
    expiry = Column(DateTime)

class ActivateUser(Base):
    __tablename__ = "ActivateUser"
    email = Column(String, primary_key=True)
    verify_key = Column(String, unique=True, index=True)
    expiry = Column(DateTime)

