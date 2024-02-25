from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

#Sub routes modules
from api.bank import bank_routes
from api.idp import idp_routes
from api.characters import characters_routes
from api.market import market_routes
from api.world import world_routes

#DB, Schemas, Models and Data
from . import schemas, models, crud, data
from .database import engine, get_db, SessionLocal

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

models.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"API": "Open Space Sky API"}

@app.post("/init")
def init_db(db: Session = Depends(get_db)):
    data.init_data(db)
    return {"API": "DB Created with Default Values"}

app.include_router(idp_routes.router)

app.include_router(bank_routes.router)

app.include_router(characters_routes.router)

app.include_router(market_routes.router)

app.include_router(world_routes.router)


