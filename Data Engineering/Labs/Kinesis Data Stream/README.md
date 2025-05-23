# Lab: Create a Kinesis Data Stream

In this lab, we created a real-time data ingestion pipeline using **Amazon Kinesis Data Streams**.
![image](https://github.com/user-attachments/assets/f6518b84-bd8c-45c1-8957-6de6a1e34fb2)


## Steps Performed

- Logged into the AWS Console using a properly permissioned IAM user (not root).
- Navigated to the **Kinesis** service and selected **Data Streams**.
- Created a new stream named `kinesis_data_stream` with:
  - **On-Demand** capacity mode (auto-managed shards)
  - Default data retention of 1 day
  - No encryption or enhanced metrics enabled

Once the stream was active, we tested it with a **Python producer script** that:
- Initialized a `boto3` Kinesis client
- Sent the current timestamp using `put_record()` API
- Printed the HTTP status code (`200` indicates success)

Finally, stream metrics were monitored using:
- **Kinesis Monitoring Dashboard**
- **Amazon CloudWatch**, where invocation graphs were confirmed
![image](https://github.com/user-attachments/assets/ddc4736f-273c-4ff8-95c8-f7b68a03b57d)
