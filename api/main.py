from fastapi import FastAPI

from .bank import bank_routes

from .idp import idp_routes

from .characters import characters_routes

from .market import market_routes

from .world import world_routes

app = FastAPI(
    title="JASK",
    description="Just Another Space Game (JASK) based on Endless Sky ",
    #summary="Space MMO based on Endless Sky ",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "url": "http://example.com/contact/",
        "email": "support@email.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

@app.get("/")
def read_root():
    return {"API": "Open Space Sky API"}

app.include_router(idp_routes.router)

app.include_router(bank_routes.router)

app.include_router(characters_routes.router)

app.include_router(market_routes.router)

app.include_router(world_routes.router)


