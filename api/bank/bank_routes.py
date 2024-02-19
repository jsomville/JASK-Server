from fastapi import APIRouter

router = APIRouter(
    prefix="/bank",
    tags=["Bank"],
)

@router.get("/transactions/")
async def get_transactions():
    #Verify Token

    #Get Character ID

    #Get Last Transactions

    #Return List Transactions

    return [{"Message": "List Of Transactions"}]


@router.post("/transfer/{character_id}")
async def transfer_to():

    #Verify Token
    
    #Verify Input Parameters
        # To Account (destination account)
        # Amout

    #Get Character ID

    #Get Character's Bank Number and Balance (Source account)

    #Verify If Balance > Amount

    #Transaction
        #Remove Amount from Source account
        #Add Amount to Destination account

    return {"Message": "Transfer Money To"}
