# pokemon_api
Testing Hosting Web Services

# Create and Connect
- docker build -t pokebase .
- docker run -p 5433:5432 -d pokebase
- python main.py
- psql -h localhost -p 5433 -U myuser -W -d mydb
