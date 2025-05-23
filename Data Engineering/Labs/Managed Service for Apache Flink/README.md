# Lab: Managed Apache Flink (Kinesis Data Analytics Replacement)

## Overview
In this lab, we explored how to deploy a streaming application using **Amazon Managed Service for Apache Flink**, which replaces the older **Kinesis Data Analytics** service.

The lab focused on:
- Using a **blueprint via CloudFormation** to automatically deploy:
  - A **Kinesis Data Stream** (source)
  - A **Managed Apache Flink application**
  - An **S3 bucket** (sink)
- Inspecting the generated **JAR file** (Apache Flink app)
- Querying output **Parquet files** in S3 using **S3 Select**
- Monitoring the Flink job via the **Apache Flink Dashboard**
- Cleaning up by deleting CloudFormation stacks and resources to avoid costs
![image](https://github.com/user-attachments/assets/7db585cb-bfa0-4a68-b032-d40011a28312)

> ⚠️ Note: This lab is **not part of the AWS Free Tier** and will incur charges if run.

---

## What We Did

### ✅ Tools & Services Used
- **CloudFormation** (to deploy blueprint)
- **Amazon Kinesis Data Streams**
- **Amazon Managed Apache Flink**
- **Amazon S3 (for output)**
- **S3 Select** (to query Parquet file contents)
- **Apache Flink Dashboard** (for real-time job metrics)
![image](https://github.com/user-attachments/assets/647381a8-503f-4dc7-a33b-d74a5b14af21)

![image](https://github.com/user-attachments/assets/adea5edf-f9ed-4acb-bee6-ebfda798080d)

### ✅ Output Observed
- JAR file uploaded to S3 for Flink job execution
- Output data stored in S3, structured in **Apache Parquet** format
- Real-time metrics in Flink UI showing ingestion rate and sink activity
![image](https://github.com/user-attachments/assets/d79ddd0b-ba53-41a8-90a3-959a40b09bb5)

---

## Cleanup Reminder
Make sure to delete:
1. The **Flink application**
2. The **Kinesis Data Stream**
3. Both **CloudFormation stacks**
To avoid ongoing charges.

---

