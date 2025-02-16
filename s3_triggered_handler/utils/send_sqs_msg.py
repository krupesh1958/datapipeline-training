"""This script send each and every content into the SQS Queue."""
import json

from uuid import uuid4
from utils import message_wrapper
from utils import queue_wrapper


qwrap = queue_wrapper.SQS()

def send_sqs(content) -> None:
    """
    Resone
    Each and every content of the script has been send into the SQS FIFO queue.
    """
    # If Queue already created; Getting the url
    # Else, create new Queue; Then getting the url
    qurl = qwrap.sqs_queue

    for i in content:
        message_wrapper.send_message(
            queue=qurl,
            message_body=json.dumps(i),
            message_grp_id=uuid4()
        )
