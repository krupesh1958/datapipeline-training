"""Connect to the mongodb."""

import os

import logging
from pymongo import MongoClient, errors


logger = logging.getLogger(__name__)

connection_string = "mongodb+srv://krupeshpatel:fMUd7FEkXi4iEbd0@cluster.svmvpud.mongodb.net/"

try:
    mongo_chat = MongoClient(host=connection_string)
except errors.ConnectionFailure as error:
    logger.error(error)

database = mongo_chat["sqs-lambda"]

# Fetch collection
user = database["testing"]
