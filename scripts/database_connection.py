import os
from pymongo import MongoClient
from dotenv import load_dotenv

class DatabaseConnection:
    """Class to manage database connections."""
    
    def __init__(self):
        """Initializes the database connection."""
        load_dotenv()
        self.mongodb_uri = os.getenv("MONGODB_URI")
    
    def get_connection(self):
        """Connects to the MongoDB database and returns the connection."""
        return MongoClient(self.mongodb_uri)