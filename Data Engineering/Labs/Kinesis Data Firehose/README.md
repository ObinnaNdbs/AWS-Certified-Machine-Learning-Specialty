# Lab: Create a Kinesis Data Firehose

This hands-on lab demonstrates how to set up an Amazon Kinesis Data Firehose that delivers streaming data from a Kinesis Data Stream into an Amazon S3 bucket.
![image](https://github.com/user-attachments/assets/d2723f5f-f941-49ef-8d15-ab8ff90e3e05)


## 🧩 Architecture Overview

**Flow:**  
`PutRecord API → Kinesis Data Stream → Kinesis Data Firehose → Amazon S3`

- **Producer:** PutRecord API sending data to Kinesis Data Streams
- **Firehose Source:** Kinesis Data Stream (created in a previous lab)
- **Firehose Destination:** Amazon S3 bucket
- **Transformation:** No transformation (Lambda disabled)
- **Compression:** None
- **Buffer Settings:** 1MB or 60 seconds
- **S3 Prefix:** `firehose/`

## 🔧 Steps Performed

1. Created a Kinesis Data Firehose Delivery Stream
2. Set the source to the previously created Kinesis Data Stream
3. Set the destination to an S3 bucket with prefix `firehose/`
4. Adjusted buffer and compression settings
5. Assigned necessary IAM permissions to Firehose
6. Ran a data producer script that sends records to the Kinesis Data Stream
7. Verified that data is successfully delivered to the S3 bucket
![image](https://github.com/user-attachments/assets/0a36dd73-005e-484f-8902-8603af24c141)

## ✅ Validation

- Verified buffered files in S3 with timestamp-based folder structure
- Opened the file to confirm real-time data was recorded with timestamps
![image](https://github.com/user-attachments/assets/b9afe7cd-4c73-4e8a-a72f-70bd4ce43e0d)
