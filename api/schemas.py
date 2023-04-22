from pydantic import BaseModel
from typing import List, Optional

class Pokemon(BaseModel):
    id: int
    name: str
    abilities: list
    japanese_name: Optional[str]
    pokedex_number: Optional[int]
    percentage_male: Optional[float]
    height_m: Optional[float]
    weight_kg: Optional[float]
    hp: Optional[int]
    attack: Optional[int]
    defense: Optional[int]
    speed: Optional[int]
    sp_attack: Optional[int]
    sp_defense: Optional[int]
    type1: Optional[str]
    type2: Optional[str]
    generation: Optional[int]
    is_legendary: Optional[bool]
    classfication: Optional[str]
    experience_growth: Optional[int]
    base_happiness: Optional[int]
    base_total: Optional[int]
    capture_rate: Optional[str]
    base_egg_steps: Optional[int]
    against_bug: Optional[float]
    against_dark: Optional[float]
    against_dragon: Optional[float]
    against_electric: Optional[float]
    against_fairy: Optional[float]
    against_fight: Optional[float]
    against_fire: Optional[float]
    against_flying: Optional[float]
    against_ghost: Optional[float]
    against_grass: Optional[float]
    against_ground: Optional[float]
    against_ice: Optional[float]
    against_normal: Optional[float]
    against_poison: Optional[float]
    against_psychic: Optional[float]
    against_rock: Optional[float]
    against_steel: Optional[float]
    against_water: Optional[float]
    pokemon_image: Optional[str]
    class Config:
        orm_mode = True
        
class SimilarPokemon(BaseModel):
    id: int
    name: str
    pokemon_image: Optional[str]
    class Config:
        orm_mode = True
        
class FullPokemon(BaseModel):
    pokemon: Pokemon
    nearest_pokemon: List[SimilarPokemon]
    class Config:
        orm_mode = True