import awsSdk

queue = awsSdk.Queue()

try:
    # Fetch Messages from queue
    print('Fetching Queue messages...')
    messages = queue.readMessages()

    # If messages is empty
    if 'Messages' not in messages:
        print('Queue is empty!')
        
    for msg in messages['Messages']:
        # Parse JSON body
        print(msg['Body'])

        # Let the queue know that the message is processed
        queue.deleteMessage(msg['ReceiptHandle'])
        print('Deleted queue message\n')
        
except Exception as ex:
    print(f"Oop's something went wrong:\n{ex}")