const AWS = require('aws-sdk');
const sqs = new AWS.SQS({
    apiVersion: '2012-11-05',
    region: 'us-east-1',
});

const getQueueUrl = async () => {
    try {
        const resp = await sqs.getQueueUrl({
            QueueName: process.env.QUEUE_NAME,
        }).promise();

        return resp['QueueUrl'];
    } catch (e) {
        return false;
    }
}

const readMessages = async (queueUrl) => {
    return await sqs.receiveMessage({
        QueueUrl: queueUrl,
        MaxNumberOfMessages: 10,
        WaitTimeSeconds: 20,
        MessageAttributeNames: ['ALL']
    }).promise();
}

const deleteMessage = async (queueUrl, receiptHandle) => {
    return await sqs.deleteMessage({
        QueueUrl: queueUrl,
        ReceiptHandle: receiptHandle,
    }).promise();
}

const delay = (time) => {
    return new Promise(resolve => setTimeout(resolve, time));
}

const startQueueProcessing = async () => {
    while(true) {
        const queueUrl = await getQueueUrl();
        const resp = await readMessages(queueUrl);
        
        if (resp.Messages?.length > 0) {
            for(let i = 0; i < resp.Messages.length; i++) {
                const {Body, ReceiptHandle} = resp.Messages[i];
                console.log('LOG: ', Body);

                // Delete message from Queue
                await deleteMessage(queueUrl, ReceiptHandle);
            }
        } else {
            console.log('Queue is empty!')
            await delay(1000 * 60) // Sleep for 1 minute
        }
    }
}

startQueueProcessing();