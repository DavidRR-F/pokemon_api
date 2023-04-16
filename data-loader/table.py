from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Pokemon(Base):
    __tablename__ = 'pokemon'

    id = Column(Integer, primary_key=True, autoincrement=True)
    abilities = relationship("Ability", back_populates="pokemon", cascade="all, delete, delete-orphan")
    against_bug = Column(Float)
    against_dark = Column(Float)
    against_dragon = Column(Float)
    against_electric = Column(Float)
    against_fairy = Column(Float)
    against_fight = Column(Float)
    against_fire = Column(Float)
    against_flying = Column(Float)
    against_ghost = Column(Float)
    against_grass = Column(Float)
    against_ground = Column(Float)
    against_ice = Column(Float)
    against_normal = Column(Float)
    against_poison = Column(Float)
    against_psychic = Column(Float)
    against_rock = Column(Float)
    against_steel = Column(Float)
    against_water = Column(Float)
    attack = Column(Integer)
    base_egg_steps = Column(Integer)
    base_happiness = Column(Integer)
    base_total = Column(Integer)
    capture_rate = Column(Integer)
    classfication = Column(String)
    defense = Column(Integer)
    experience_growth = Column(Integer)
    height_m = Column(Float)
    hp = Column(Integer)
    japanese_name = Column(String)
    name = Column(String)
    percentage_male = Column(Float)
    pokedex_number = Column(Integer)
    sp_attack = Column(Integer)
    sp_defense = Column(Integer)
    speed = Column(Integer)
    type1 = Column(String)
    type2 = Column(String)
    weight_kg = Column(Float)
    generation = Column(Integer)
    is_legendary = Column(Boolean)
    pokemon_image = Column(String)
    
class Ability(Base):
    __tablename__ = 'ability'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    pokemon_id = Column(Integer, ForeignKey('pokemon.id'))
    pokemon = relationship("Pokemon", back_populates="abilities")
    
    #psql -h host -p port -U user -W -d database
    