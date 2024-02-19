from pydantic import BaseModel
#from pydantic import EmailStr

class User(BaseModel):
    firstname: str
    lastname: str
    email: str

class NewUser(User):
    password: str

class RegisteredUser(User):
    id : str
    hashedPassword : str
    emailVerifiedTag: str
    emailVerified: bool | None = None
    
class Credentials(BaseModel):
    email : str
    password : str


class Token(BaseModel):
    token : str