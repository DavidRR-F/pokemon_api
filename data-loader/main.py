import pandas as pd
import ast
import csv
import base64
from constants import DATABASE_URL, IMG_FOLDER, CSV_FILE, IMG_NAMES
from table import Ability, Pokemon
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def image_to_base64(image_path: str) -> str:
    with open(image_path, 'rb') as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
    
def get_image_base64(name: str) -> str:
    if not name == "Type: Null":
        formatted_name = format_name(name)
        return f"{formatted_name}.png"

def format_name(name: str) -> str:
    formatted_name = name.replace("'", "").replace(" ", "").replace(".", "-").replace("é", "e").lower()
    match formatted_name:
        case _ if "♀" in formatted_name:
            return formatted_name[:-1] + "-f"
        case _ if "♂" in formatted_name:
            return formatted_name[:-1] + "-m"
        case "mimejr-":
            return formatted_name[:-3] + "-jr"
        case _ if "tapu" in formatted_name:
            return formatted_name[:4] + "-" + formatted_name[4:]
        case _:
            for image_name in IMG_NAMES:
                if image_name.startswith(formatted_name):
                    return image_name
            return formatted_name

def get_abilities(abilities):
    ability_objects = []
    for ability in abilities:
        ability_objects.append({
            "name": ability
        })
    return ability_objects

def add_pokemon(pokemon_data):
    abilities = get_abilities(ast.literal_eval(pokemon_data['abilities']))
    del pokemon_data['abilities']
    new_pokemon = Pokemon(**pokemon_data)
    for ability in abilities:
        ability = Ability(**ability)
        new_pokemon.abilities.append(ability)
    return new_pokemon

def create_db():
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    data = pd.read_csv(CSV_FILE)
    data['pokemon_image'] = data['name'].apply(get_image_base64)
    #print(data)
    for _, row in data.iterrows():
        pokemon_data = row.to_dict()
        session.add(add_pokemon(pokemon_data))
    session.commit()
    
if __name__ == "__main__":
    create_db()