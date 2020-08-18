import os
from pymongo import MongoClient
DATABASE_URI = os.environ.get('DATABASE_URI',"default_value")
cluster = MongoClient("mongodb+srv://admin:nydqqzuy1324@cluster0-oobol.mongodb.net/")
db = cluster.eceSite