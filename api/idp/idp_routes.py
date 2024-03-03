import datetime
import random
import string
from fastapi import Depends, APIRouter, HTTPException, status
import jwt
from sqlalchemy.orm import Session

from api.dependency import getUser

from api import crud, schemas
from api.database import SessionLocal, engine, get_db

import hashlib

TOKEN_SECRET="simpleSecret!!!"

router = APIRouter(
    prefix="/idp",
    tags=["IDP"],
)

@router.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users    

@router.post("/login/", response_model=schemas.Token)
@router.post("/login/")
async def login(credentials: schemas.Credentials, db: Session = Depends(get_db)):

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
    # User email
    # Character ID
    # Expiry DateTime
    data = dict()
    data["email"] = user.email
    data["character"] = 1
    expiry =(datetime.datetime.now() + datetime.timedelta(hours=24))
    data["expiry"] = expiry.isoformat()
    token = jwt.encode(data, TOKEN_SECRET, algorithm="HS256")
    print(token)

    #Add Token To DB
    #TODO --> to cache only
    token_hash = hashlib.md5(token.encode()).hexdigest()
    print(token_hash)
    crud.remove_token_by_email(db, user.email)
    crud.create_token(db, token_hash, user.email, expiry)
    print("HERE !!")

    return token


@router.post("/logout/")
async def logout(token: schemas.Token):

    #Verify Token
    token_str = crud.get_token(token)
    
    #Delete Token From Cache
    crud.remove_token(token)

    return [{"Message": "Logout"}]


@router.post("/register/")
async def register(user: schemas.UserFormCreate, db: Session = Depends(get_db)):

    #Verify Is user is not used
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered") 

    #Create User
    u = schemas.UserCreate
    u.email = user.email
    u.firstname = user.firstname
    u.lastname = user.lastname
    u.password = user.password
    u.is_active = False
    crud.create_user(db, u)

    #Generate Confirmation Key
    lenght = 6
    confirmation_key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=lenght))
    print(f"Confirmation Key : {confirmation_key}")

    #Store Confirmation Key
    crud.create_activateKey(db, confirmation_key, user.email)

    #Send email confirmation
    #TODO SEND MAIL

    return [{"Message": "User Registered"}]


@router.post("/verifyemail/{verification_key}")
async def verify_email(verification_key, db: Session = Depends(get_db)):

    #Verify email Verification ID
    email_key = crud.get_activateKey(db, verification_key)
    if not email_key:
        raise HTTPException(status_code=400, detail="Invalid Key") 
    

    #Set User Verified flag
    crud.activate_user(db, email_key.email)

    #Clear Verification Tag
    crud.remove_activateKey(db, verification_key)

    return [{"Message": "Email Verified"}]