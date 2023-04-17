from fastapi import FastAPI, HTTPException
from tortoise.contrib.fastapi import register_tortoise
from model import Pokemon

app = FastAPI()

register_tortoise(
    app,
    db_url="postgres://myuser:mypassword@db:5432/mydb",
    modules={"models": ["main"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/pokemon/{pokemon_id}")
async def get_pokemon(pokemon_id: int):
    pokemon = await Pokemon.get_or_none(id=pokemon_id)
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return pokemon