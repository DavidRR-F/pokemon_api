from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.dialects.postgresql import JSON
from pgvector.sqlalchemy import Vector

from pokemon_api.database import Base

class Pokemon(Base):
    __tablename__ = 'pokemon'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    abilities = Column(JSON)
    japanese_name = Column(String(255), nullable=True)
    pokedex_number = Column(Integer, nullable=True)
    percentage_male = Column(Float, nullable=True)
    height_m = Column(Float, nullable=True)
    weight_kg = Column(Float, nullable=True)
    hp = Column(Integer, nullable=True)
    attack = Column(Integer, nullable=True)
    defense = Column(Integer, nullable=True)
    speed = Column(Integer, nullable=True)
    sp_attack = Column(Integer, nullable=True)
    sp_defense = Column(Integer, nullable=True)
    type1 = Column(String(50), nullable=True)
    type2 = Column(String(50), nullable=True)
    generation = Column(Integer, nullable=True)
    is_legendary = Column(Boolean, nullable=True)
    classfication = Column(String(255), nullable=True)
    experience_growth = Column(Integer, nullable=True)
    base_happiness = Column(Integer, nullable=True)
    base_total = Column(Integer, nullable=True)
    capture_rate = Column(String(10), nullable=True)
    base_egg_steps = Column(Integer, nullable=True)
    against_bug = Column(Float, nullable=True)
    against_dark = Column(Float, nullable=True)
    against_dragon = Column(Float, nullable=True)
    against_electric = Column(Float, nullable=True)
    against_fairy = Column(Float, nullable=True)
    against_fight = Column(Float, nullable=True)
    against_fire = Column(Float, nullable=True)
    against_flying = Column(Float, nullable=True)
    against_ghost = Column(Float, nullable=True)
    against_grass = Column(Float, nullable=True)
    against_ground = Column(Float, nullable=True)
    against_ice = Column(Float, nullable=True)
    against_normal = Column(Float, nullable=True)
    against_poison = Column(Float, nullable=True)
    against_psychic = Column(Float, nullable=True)
    against_rock = Column(Float, nullable=True)
    against_steel = Column(Float, nullable=True)
    against_water = Column(Float, nullable=True)
    pokemon_image = Column(String(1000), nullable=True)
    image_vector = Column(Vector(2048))