import requests
from pydantic import ValidationError

from src.domain.pokemon_row import PokemonModel


def fetch_pokemon_data(url, pokemon_id):
    try:
        response = requests.get(url + str(pokemon_id))
        if response.status_code == 200:
            pokemon_data = response.json()
            pokemon = PokemonModel(**pokemon_data)
            return pokemon
        else:
            print(f"La requête a échoué avec le code de statut {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Une erreur s'est produite lors de la requête : {e}")
        return None
    except ValidationError as e:
        print(f"Erreur de validation du modèle : {e}")
        return None
