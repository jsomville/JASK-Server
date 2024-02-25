from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session

from ..schemas import Credentials, Token

from api.dependency import getUser

from api import crud, schemas
from api.database import SessionLocal, engine, get_db

import hashlib

router = APIRouter(
    prefix="/idp",
    tags=["IDP"],
)

@router.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users    

@router.post("/login/", response_model=Token)
async def login(credentials: Credentials, db: Session = Depends(get_db)):

    #Verify Input Parameters
    email = credentials.email
    password = credentials.password

    #Verrify if Credentials Exists
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    user = crud.get_user_by_email_and_hashed_password(db, email, hashed_password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    

    #Verify if email is validated
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication requires email verification",
            headers={"WWW-Authenticate": "Bearer"},
        )

    #Generate a Token
    var =  hashlib.sha256(user.email.encode()).hexdigest()
    token = Token(tokenStr=var)
    
    #Add Token To cache

    #Return a Token
    return token


@router.post("/logout/")
async def logout():

    #Verify Token

    #Delete Token From Cache

    return [{"Message": "Logout"}]


@router.post("/register/")
async def register(user: schemas.UserCreate, db: Session = Depends(get_db)):

    #Verify Is user is not used
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered") 

    #Create User
    crud.create_user(db=db, user=user)

    #Generate email Confirmation ID

    #Send email confirmation

    return [{"Message": "User Registered"}]


@router.post("/verifyemail/{email_verification_id}")
async def verify_email():

    #Verify email Verification ID

    #Set User Verified flag

    #Clear Verification Tag

    return [{"Message": "Email Verified"}]