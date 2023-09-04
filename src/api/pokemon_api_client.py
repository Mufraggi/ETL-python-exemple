import requests
from pydantic import ValidationError

from src.domain.pokemon_raw import PokemonModel


def fetch_pokemon_data(url, pokemon_id):
    try:
        response = requests.get(url + str(pokemon_id))
        if response.status_code == 200:
            pokemon_data = response.json()
            pokemon = PokemonModel(**pokemon_data)
            return pokemon
        else:
            print(f"The request failed with status code {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {e}")
        return None
    except ValidationError as e:
        print(f"An error occurred during the request: {e}")
        return None
