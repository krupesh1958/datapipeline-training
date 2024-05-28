"""This lambda function triggered when the upload new file into s3 bucket."""
from __future__ import annotations

import boto3
from urllib.parse import unquote_plus
from threading import Thread

from utils import send_sqs_msg as send_message


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

    print("Testing code:", str(file_obj["s3"]["object"]["key"]))
    print("Testing code:", unquote_plus(str(file_obj["s3"]["object"]["key"])))

    file_obj = s3.get_object(Bucket=bucket_name, key=key)
    file_content = file_obj["Body"].read().decode("utf-8")

    # Let's put file_content into the SQS Queue.
    # We assume file_content type is List.
    Thread(target=send_message, args=(file_content, ), daemon=True).start()
    return {
        "statusCode": 200,
        "message": "Data has been send into the SQS Queue."
    }
