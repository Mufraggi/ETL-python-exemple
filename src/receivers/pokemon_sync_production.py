import json

from bson import ObjectId

from src.repository.pokemon_production_repository import get_pokemon_Production_repository
from src.repository.pokemon_row_repository import get_pokemon_row_repository

repository_row = get_pokemon_row_repository()
repository_prod = get_pokemon_Production_repository()

queue_sync_production = 'pokemon_sync_production'


def callback_pokemon_sync_production(ch, method, properties, body):
    message_body = body.decode('utf-8')
    message_data = json.loads(message_body)
    id_value = message_data.get('id')
    row_pokemon = repository_row.find_one_by_id(ObjectId(id_value))
    repository_prod.insert(clean_data(row_pokemon))


def clean_data(data):
    return {
        "row_id": data.get("_id"),
        "pokedexId": data.get("pokedexId"),
        "generation": data.get("generation"),
        "name": data.get("name").get("fr"),
        "stats": data.get("stats")
    }
