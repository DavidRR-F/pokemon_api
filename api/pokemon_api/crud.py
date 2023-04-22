from typing import List, Tuple
from sqlalchemy.orm import Session
from sqlalchemy import select, func

from pokemon_api.schemas import FullPokemon, Pokemon, SimilarPokemon
from pokemon_api.models import Pokemon as PokemonModel

import pokemon_api.models as models

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
    
def get_pokemon_and_nearest(db: Session, pokemon_id: int) -> Tuple[Pokemon, List[SimilarPokemon]]:
    pokemon = get_pokemon(db, pokemon_id)
    nearest = get_nearest(db, pokemon_id)
    return FullPokemon(pokemon=pokemon, nearest_pokemon=nearest)