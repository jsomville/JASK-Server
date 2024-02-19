from fastapi import APIRouter

router = APIRouter(
    prefix="/market",
    tags=["Market"],
)

@router.get("/buyorder/")
async def get_buy_order():

    #Verify Token

    #Get a List of Orders

    #Return the List of Order

    return [{"Message": "Get Buy Order List"}]


@router.get("/buyorder/{id}")
async def get_buy_order(id):

    #Verify Token

    #Verify the input parameter

    #Get a the Order

    #Return the Order

    return [{"Message": "Get Buy Order"}]


@router.post("/buyorder/")
async def create_buy_order(id):

    #Verify Token

    #Verify the input parameter

    #Create the Order


    return [{"Message": "Buy Order Created"}]


@router.delete("/buyorder/")
async def cancel_buy_order(id):

    #Verify Token

    #Verify the input parameter

    #Cancel the Order


    return [{"Message": "Buy Order Cancelled"}]


@router.get("/sellorder/")
async def get_sell_order():

    #Verify Token

    #Get a List of Sell Order

    #Return the List of Order

    return [{"Message": "Get Sell Orders List"}]


@router.get("/sellorder/{id}")
async def get_sell_order(id):

    #Verify Token

    #Verify the input parameter

    #Get a the Order

    #Return the Order

    return [{"Message": "Get Sell Order"}]


@router.post("/sellorder/")
async def create_sell_order(id):

    #Verify Token

    #Verify the input parameter

    #Create the Order


    return [{"Message": "Sell Order Created"}]


@router.delete("/sellorder/")
async def cancel_sell_order(id):

    #Verify Token

    #Verify the input parameter

    #Cancel the Order


    return [{"Message": "Buy Order Cancelled"}]

@router.get("/ressource/")
async def get_ressource():

    #Verify Token

    #Verify the input parameter

    #Get a the List Of Ressource by Category

    #Return the Order

    return [{"Message": "Get Ressource"}]
