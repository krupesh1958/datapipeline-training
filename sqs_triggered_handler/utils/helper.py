"""This script has been store all messages into the MongoDB"""
from typing import List
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


def store_mongo(messages: List[dict]) -> None:
    """
    Function will store every single messages into the mongodb with seprate 
    documents.
    """
    for num, i in enumerate(messages):
        i["Sequence"] = num
        user.insert_one(document=i)
    return
