from pymongo import MongoClient


class Connection:
    def __init__(self, database):
        self.client = MongoClient('mongodb://localhost:27017')
        self.db = self.client[database]

    def get_all(self, collection, condition={}, select={}):
        collect = self.db[collection]
        result = collect.find(condition, select)
        return list(result)
    def get_all_validacion(self, collection, condition={}):
        collect = self.db[collection]
        result = collect.find(condition)
        return list(result)

    def get_one(self, collection, condition={}, select={}):
        collect = self.db[collection]
        result = collect.find_all(condition, select)
        return result

    def insert(self, collection, data):
        collect = self.db[collection]
        result = collect.insert_one(data)
        print(f'Insert Document -> {result.inserted_id}')
        return result.inserted_id

    def insert_many(self, collection, data):
        collect = self.db[collection]
        result = collect.insert_many(data)
        print(f'Insert Documents -> {result.inserted_ids}')

    def update(self, collection, condition, change, upsert=False):
        collect = self.db[collection]
        collect.update_one(condition, {
            "$set": change
        }, upsert=upsert)
        print(f'Update Document')

    def update_many(self, collection, condition, change):
        collect = self.db[collection]
        result = collect.update_many(condition, {
            "$set": change
        })
        print(F'Update Documents -> {result.raw_result} - Match -> {result.matched_count}')

    def delete(self, collection, condition):
        collect = self.db[collection]
        collect.delete_one(condition)
        print(f'Delete Document')

    def delete_many(self, collection, condition):
        collect = self.db[collection]
        result = collect.delete_many(condition)
        print(f'Delete Documents -> {result.deleted_count}')



