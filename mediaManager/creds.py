import os
from pymongo import MongoClient
DATABASE_URI = os.environ.get('DATABASE_URI')
cluster = MongoClient(DATABASE)
db = cluster.eceSite