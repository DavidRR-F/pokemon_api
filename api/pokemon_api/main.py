from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import pokemon_api.crud as crud
import pokemon_api.models as models
import pokemon_api.schemas as schemas
from pokemon_api.database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to the list of allowed origins or a specific origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/pokemon", response_model=list[schemas.Pokemon])
def get_all_pokemon(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pokemon = crud.get_all_pokemon(db, skip=skip, limit=limit)
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return pokemon

@app.get("/pokemon/{pokemon_id}", response_model=schemas.Pokemon)
def get_pokemon(pokemon_id: int, db: Session = Depends(get_db)):
    pokemon = crud.get_pokemon(db, pokemon_id=pokemon_id)
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return pokemon

@app.get("/pokemon/{pokemon_id}/similar", response_model=schemas.FullPokemon)
def get_pokemon(pokemon_id: int, db: Session = Depends(get_db)):
    pokemon = crud.get_pokemon_and_nearest(db, pokemon_id)
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return pokemon