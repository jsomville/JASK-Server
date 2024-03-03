from typing import Optional, List, Tuple
from pydantic import BaseModel
#from pydantic import EmailStr

class UserBase(BaseModel):
    email: str

class UserFormCreate(UserBase):
    password: str
    firstname : str
    lastname : str

class UserCreate(UserFormCreate):
    is_active : bool

    
class User(UserBase):
    id: int
    is_active: bool
    firstname: str
    lastname: str

    class Config:
        orm_mode = True
    
class Credentials(BaseModel):
    email : str
    password : str


class Token(BaseModel):
    tokenStr : str

class SolarObject(BaseModel):
    name : Optional[str]
    sprite : str
    distance : int
    period : int

class SolarSystem(BaseModel):
    name: str
    position : Tuple[int,int]
    governement: str
    links: Optional[List[str]]
    objects : List[SolarObject]

class Map(BaseModel):
    SolarSystems : List[SolarSystem]