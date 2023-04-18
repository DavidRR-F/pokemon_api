from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models,schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

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