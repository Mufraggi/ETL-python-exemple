import json

from src.api.pokemon_api_client import fetch_pokemon_data
from src.receivers.pokemon_sync_production import queue_sync_production
from src.repository.pokemon_row_repository import get_pokemon_row_repository

repository = get_pokemon_row_repository()

queue_api_sync = 'pokemon_sync_api'


def callback_pokemon_api_call(ch, method, properties, body):
    message_body = body.decode('utf-8')
    message_data = json.loads(message_body)
    id_value = message_data.get('id')
    pokemon = fetch_pokemon_data("https://api-pokemon-fr.vercel.app/api/v1/pokemon/", id_value)
    created = repository.insert(pokemon.dict())

    message = json.dumps({"id": str(created.inserted_id)})
    ch.basic_publish(exchange='', routing_key=queue_sync_production, body=message)
