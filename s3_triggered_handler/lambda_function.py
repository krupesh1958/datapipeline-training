"""This lambda function triggered when the upload new file into s3 bucket."""
from __future__ import annotations

import json
import boto3
from urllib.parse import unquote_plus
from threading import Thread

from utils.send_sqs_msg import send_sqs as send_message


def lambda_handler(event, context):
    """
    This function handler the s3 bucket request when the user upload new file into s3 bucket
    """
    s3 = boto3.client("s3")

    if not event:
        return {
            "statusCode": 404,
            "message": "Sorry, we don't have found the event logs"
        }
    
    file_obj = event["Records"][0]
    bucket_name = str(file_obj["s3"]["bucket"]["name"])
    key = unquote_plus(str(file_obj["s3"]["object"]["key"]))

    print("bucket_name: %s" % bucket_name)
    print("s3 bucket key: %s" % key)

    file_obj = s3.get_object(Bucket=bucket_name, Key=key)
    file_content = file_obj["Body"].read().decode("utf-8")

    # Let's put file_content into the SQS Queue.
    # We assume file_content type is List.
    send_message(json.loads(file_content))
    return {
        "statusCode": 200,
        "message": "Data has been send into the SQS Queue."
    }
