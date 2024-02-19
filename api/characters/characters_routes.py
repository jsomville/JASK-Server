from fastapi import APIRouter

router = APIRouter(
    prefix="/characters",
    tags=["Characters"],
)

@router.get("/")
async def get_characters_list():
    #Verify Token

    #Get List Of characters

    #Get Last Characters

    #Return List Characters

    return [{"Message": "List Of Characters"}]


@router.get("/{character_id}")
async def get_characters():
    # --> Must implement paginations ...
    
    #Verify Token

    #Verify character_id

    #Get Character Detail

    #Return  Characters Detail

    return [{"Message": "Get character detail"}]