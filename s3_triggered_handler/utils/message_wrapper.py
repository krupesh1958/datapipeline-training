"""This file push all content into SQS."""
from typing import Union

from botocore.exceptions import ClientError


class JsonResponse(object): ...

MessageType = Union[ClientError, JsonResponse]


class SQSQueueURL(object):
    ...


def send_message(
    queue: SQSQueueURL,
    message_body: str,
    message_grp_id: int = 0,
    mesage_attribute = None
):
    """
    Send a message to an Amazon SQS queue.

    :param queue: The queue that receives the message.
    :param message_body: The body text of the message.
    :param message_attributes: Custom attributes of the message. These are key-value
                            pairs that can be whatever you want.
    :return: The response from SQS that contains the assigned message ID.
    """
    if not mesage_attribute:
        mesage_attribute = {}

    try:
        response = queue.send_message(
            MessageBody=message_body,
            MessageAttributes=mesage_attribute,
            MessageGroupId=str(message_grp_id),
            MessageDeduplicationId=str(message_grp_id)
        )
    except ClientError as error:
        print("Send message failed: %s" % message_body)
        print("Exception generation: %s" % error)
        raise
    else:
        return response
