from pymongo import MongoClient


class PokemonProductionRepository:
    def __init__(self, db_url, db_name, collection_name):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert(self, data):
        return self.collection.insert_one(data)


def get_pokemon_Production_repository():
    db_url = "mongodb://localhost:27018/"  # L'URL de connexion MongoDB
    db_name = "Prod"
    collection_name = "pokemon"

    return PokemonProductionRepository(db_url, db_name, collection_name)
