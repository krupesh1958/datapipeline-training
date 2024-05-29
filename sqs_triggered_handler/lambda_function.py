"""This function trigere when the handler call."""
import boto3

from util import store_mongo as send_message

def lambda_handler(event, context):
    """
    This function handler request when the sqs triggered the function.
    """

    if not event:
        return {
            "statusCode": 404,
            "message": "Sorry, we don't have found the event logs"
        }

    messages = event["Records"]
    
    print("Fetching the all messages from the SQS: ", messages)

    # Now send this all batch messages into the MongoDB.
    send_message(messages=messages["body"])
    return {
        "statusCode": 200,
        "message": "Data has been send into the SQS Queue."
    }
