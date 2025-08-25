# mongo_config.py
import os

import pymongo

# MongoDB connection settings (update with your connection string)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

def connect_db():
    return pymongo.MongoClient(MONGO_URI)
