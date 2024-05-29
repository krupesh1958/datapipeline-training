"""This script has been store all messages into the MongoDB"""
from typing import List

from sqs_triggered_handler import user



def store_mongo(messages: List[dict]) -> None:
    """
    Function will store every single messages into the mongodb with seprate 
    documents.
    """
    for i in messages:
        user.insert_one(document=i)
    return
