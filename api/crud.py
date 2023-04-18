from sqlalchemy.orm import Session

from . import models

def get_pokemon(db: Session, pokemon_id: int):
    return db.query(models.Pokemon).filter(models.Pokemon.id == pokemon_id).first()

def get_all_pokemon(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Pokemon).offset(skip).limit(limit).all()