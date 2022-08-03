from pymongo import MongoClient
import pymongo
from pymongo import MongoClient

CONNECTION_STRING = "mongodb://mongodb0.example.com:27017/CacheDb"


def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['LunaData']


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
    # Get the database
    dbname = get_database()
