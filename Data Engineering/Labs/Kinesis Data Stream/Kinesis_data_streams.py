import boto3
import json
from datetime import datetime
from time import sleep

# Initialize Kinesis client
kinesis = boto3.client('kinesis', region_name='us-east-1')
stream_name = 'Kinesis_Data_Stream'

# Send timestamp data to the stream
for i in range(900):
    current_time = datetime.now().strftime("%H:%M:%S")
    payload = {'data': current_time}
    
    response = kinesis.put_record(
        StreamName=stream_name,
        Data=json.dumps(payload),
        PartitionKey='partition'
    )
    
    print(response)
    sleep(1)
