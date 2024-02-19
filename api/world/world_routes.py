from fastapi import APIRouter

router = APIRouter(
    prefix="/world",
    tags=["World"],
)

@router.post("/dock/")
async def dock():

    #Verify Token

    #Set character dock

    #Return ?

    return [{"Message": "Dock"}]

@router.post("/undock/")
async def undock():

    #Verify Token

    #Set character undock

    #Return the url of RT server

    return [{"Message": "Undock"}]

@router.post("/warpto/{id}")
async def warp_to():

    #Verify Token

    #Set character dock

    #Return ?

    return [{"Message": "Warp to"}]

@router.get("/solarsystems/")
async def get_solar_systems():

    #Verify Token

    #Get SS List

    #Return SS List

    return [{"Message": "Solar System List"}]


@router.get("/solarsystems/{id}}")
async def get_solar_systems_detail():

    #Verify Token

    #Get SS Detail

    #Return SS Detail

    return [{"Message": "Solar System Detail"}]


@router.get("/jumpbridge/")
async def get_jump_bridge():

    #Verify Token

    #Get JB List

    #Return JB List

    return [{"Message": "Solar Jump Bridge List"}]