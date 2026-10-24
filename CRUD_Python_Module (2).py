from pymongo import MongoClient


class AnimalShelter:
    """Provide CRUD operations for the Austin Animal Center collection."""

    def __init__(self, username, password):
        """Initialize the MongoDB client and connect to the AAC animals collection."""
        user = username
        password_value = password
        host = "localhost"
        port = 27017
        database_name = "aac"
        collection_name = "animals"

        self.client = MongoClient(
            "mongodb://%s:%s@%s:%d" % (user, password_value, host, port)
        )
        self.database = self.client[database_name]
        self.collection = self.database[collection_name]

    def create(self, data):
        """Insert one document and return True when the insert succeeds."""
        if not data:
            return False

        try:
            self.collection.insert_one(data)
            return True
        except Exception as error:
            print("Create operation failed:", error)
            return False

    def read(self, query):
        """Return all documents matching query as a Python list."""
        if query is None:
            return []

        try:
            cursor = self.collection.find(query)
            return list(cursor)
        except Exception as error:
            print("Read operation failed:", error)
            return []

    def update(self, query, update_data):
        """Update all documents matching query and return the modified count."""
        if query is None or not update_data:
            return 0

        try:
            result = self.collection.update_many(query, update_data)
            return result.modified_count
        except Exception as error:
            print("Update operation failed:", error)
            return 0

    def delete(self, query):
        """Delete all documents matching query and return the deleted count."""
        if query is None:
            return 0

        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as error:
            print("Delete operation failed:", error)
            return 0
