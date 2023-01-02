import os
import boto3

# # # # # # # # # # # # # #
# Queue                   #
# # # # # # # # # # # # # #
class Queue():
    def __init__(self):
        client =  boto3.client('sqs')
        response = client.get_queue_url(QueueName=os.getenv('QUEUE_NAME'))
        self.queueUrl = response['QueueUrl']
        self.sqs = boto3.client('sqs', endpoint_url=self.queueUrl)

    def sendMessage(self, msg):
        return self.sqs.send_message(
            QueueUrl=self.queueUrl,
            MessageBody=msg
        )

    def readMessages(self):
        return self.sqs.receive_message(
            QueueUrl=self.queueUrl,
            # AttributeNames=[
            #     'SentTimestamp'
            # ],
            MaxNumberOfMessages=10,
            WaitTimeSeconds=20,
            MessageAttributeNames=[
                'All'
            ]
        )

    def deleteMessage(self, receiptHandle):
        return self.sqs.delete_message(
            QueueUrl=self.queueUrl,
            ReceiptHandle=receiptHandle
        )
