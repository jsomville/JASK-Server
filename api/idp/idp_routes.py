from fastapi import APIRouter

router = APIRouter(
    prefix="/idp",
    tags=["IDP"],
)

from .model import Credentials, NewUser, RegisteredUser, Token

@router.post("/login/", response_model=Token)
async def login(credentials: Credentials):

    #Verify Input Parameters

    #Verify UN + Pass corresponds to an existing user

    #Verify if email is validated

    #Generate a Token

    #Add Token To chache

    #Return a Token

    return [{"Message": "Login"}]

@router.post("/logout/")
async def logout():

    #Verify Token

    #Delete Token From Cache

    return [{"Message": "Logout"}]


@router.post("/register/")
async def register():

    #Verify Input Parameters

    #Verify email not used

    #Hash Password

    #Add User Parameters in DB

    #Generate email Confirmation ID

    #Send email confirmation

    return [{"Message": "Register"}]


@router.post("/verifyemail/{email_verification_id}")
async def verify_email():

    #Verify email Verification ID

    #Set User Verified flag

    return [{"Message": "Email Verified"}]