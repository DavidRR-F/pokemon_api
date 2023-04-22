from sqlalchemy.orm import Session
from sqlalchemy import select, func
from api.models import Pokemon as PokemonModel
from api.schemas import Pokemon

from . import models

def get_pokemon(db: Session, pokemon_id: int):
    return db.query(models.Pokemon).filter(models.Pokemon.id == pokemon_id).first()

def get_all_pokemon(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Pokemon).offset(skip).limit(limit).all()

def get_nearest(db: Session, pokemon_id: int):
    return db.execute((
        select(PokemonModel.id, PokemonModel.name, PokemonModel.pokemon_image)
        .where(PokemonModel.id != pokemon_id)
        .order_by(
            func.abs(
                PokemonModel.image_vector.op('<->')( 
                    db.query(PokemonModel.image_vector).filter(PokemonModel.id == pokemon_id).scalar() 
                )
            )
        ).limit(12)
    )).fetchall()