from pymongo import MongoClient
from pymongo.errors import ConfigurationError

class MongoDBHandler:
    def __init__(self, uri='mongodb://localhost:27017/', database_name='bot_scrape'):
        self.uri = uri
        self.database_name = database_name
        self.client = None
        self.db = None
        self.connect()
    
    def connect(self):
        try:
            self.client = MongoClient(self.uri)
            self.db = self.client[self.database_name]
            print(f"Connected to MongoDB at {self.uri}, using database: {self.database_name}")
        except ConfigurationError as e:
            print(f"Failed to connect to MongoDB: {e}")
    
    def insert_one(self, collection_name, document):
        collection = self.db[collection_name]
        result = collection.insert_one(document)
        return result.inserted_id
    
    def find_one(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.find_one(query)
    
    def find_all(self, collection_name, query={}):
        collection = self.db[collection_name]
        return list(collection.find(query))
    
    def update_one(self, collection_name, query, update_values):
        collection = self.db[collection_name]
        result = collection.update_one(query, {'$set': update_values})
        return result.modified_count
    
    def delete_one(self, collection_name, query):
        collection = self.db[collection_name]
        result = collection.delete_one(query)
        return result.deleted_count
    
    def close_connection(self):
        if self.client:
            self.client.close()
            print("Connection to MongoDB closed")