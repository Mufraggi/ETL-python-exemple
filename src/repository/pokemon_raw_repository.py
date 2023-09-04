from pymongo import MongoClient


class PokemonRawRepository:
    def __init__(self, db_url, db_name, collection_name):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert(self, data):
        return self.collection.insert_one(data)

    def find_one_by_id(self, id):
        return self.collection.find_one({"_id": id})


def get_pokemon_row_repository():
    db_url = "mongodb://localhost:27017/"
    db_name = "data_warehouse"
    collection_name = "pokemon"

    return PokemonRawRepository(db_url, db_name, collection_name)
