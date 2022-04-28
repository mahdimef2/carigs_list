import json
from abc import ABC, abstractmethod

from mongo import MongoDatabase


class StorageAbstract(ABC):
    @abstractmethod
    def store(self, data, *args):
        pass

    @abstractmethod
    def loads(self):
        pass


class MongoStorage(StorageAbstract):
    def __init__(self):
        self.mongo = MongoDatabase()

    def store(self, data, collection, *args):
        collection = getattr(self.mongo.database, collection)
        if isinstance(data, list) and len(data) > 1:
            collection.insert_many(data)
        else:
            collection.insert_one(data)

    def loads(self):
        return self.mongo.database.adv_links.find({'flag': False})

    def update_flag(self, data):
        self.mongo.database.adv_links.find_one_and_update(
            {'_id': data['_id']},
            {'$set': {'flag': True}}
        )


class FileStorage(StorageAbstract):
    def store(self, data, filename, *args):
        with open(f'data/adv/{filename}.json', 'w') as f:
            f.write(json.dumps(data))
        print(f'data/adv/{filename}.json')

    def loads(self):
        with open('data/adv/adv_links.json', 'r') as f:
            links = json.loads(f.read())
        return links
