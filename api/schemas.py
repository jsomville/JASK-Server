from pydantic import BaseModel
#from pydantic import EmailStr

class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str
    firstname : str
    lastname : str

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