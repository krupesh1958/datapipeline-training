"""
Resone:

This script for delete, get, and create new queue:
"""
from typing import Union

import boto3
from botocore.errorfactory import ClientError

boto_sqs = boto3.resource("sqs")

class JsonResponse(object): ...

MessageType = Union[ClientError, JsonResponse, None]


class SQS:

    def __init__(self) -> None:
        self._sqs_queue = None
        self._sqs_queue_url = None

    @property
    def sqs_queue(self) -> MessageType:
        """
        Gets an SQS queue by name.

        :param name: The name that was used to create the queue.
        :return: A Queue object.
        """
        try:
            queue = boto_sqs.get_queue_by_name(QueueName=self._name)
            print("Got queue '%s' with URL=%s", self._name, queue.url)
        except ClientError as error:
            print("Couldn't get queue named %s.", self._name)
            raise
        else:
            self._sqs_queue_url = queue
            return queue

    @sqs_queue.setter
    def sqs_queue(self, name: str, **attributes) -> None:
        """
        Creates an Amazon SQS queue.

        :param name: The name of the queue.
        :param attributes: The attributes of the queue, such as maximum message size
        or whether it's a FIFO queue.
        :return: A queue object that contains metadata about the queueu and that can be
        used to perform queue operations like spending and receiving messages.
        """
        if not attributes:
            attributes = {
                "FifoQueue": "true"
            }
        try:
            queue = boto_sqs.create_queue(QueueName=name, Attributes=attributes)
            print("Created queue '%s' with URL=%s", name, queue.url)
        except ClientError as error:
            print("Couldn't create queue named '%s'.", name)
            raise error
        else:
            self._name = name

    @sqs_queue.deleter
    def sqs_queue(self):
        """
        Remove an Amazon SQS queue.
        Once, object has been deleted you should wait atleas 60 seconds to create new queue as per the AWS policy.

        :param name: The name of the queue.
        :return: Return boolen field; if true that means object removed, else raise error
        """
        try:
            self._sqs_queue_url.delete()
            print("Deleted queue url=%s", self._sqs_queue_url)
        except ClientError as error:
            print("Couldn't delete queue with URL=%s!", self._sqs_queue_url)
            raise error
