# Lab: AWS Glue ETL – Convert JSON to Parquet

In this lab, we used **AWS Glue Visual ETL** to convert a dataset stored in **JSON** format to **Parquet** format, compress it using **Snappy**, and save it to Amazon S3. This was done entirely through the Glue Studio visual interface without writing any code.

## 🔧 Steps Performed

1. **Created a Visual ETL Job** named `convert ticker demo from JSON to Parquet`.
   ![image](https://github.com/user-attachments/assets/5847a71e-bc4c-487e-87ca-0162214158b1)

3. **Data Source**: Amazon S3 (selected from the Glue Data Catalog).
4. **Transformation**: Applied the `Change Schema` transformation.
5. **Target**: Amazon S3 with output format set to **Parquet** and compression set to **Snappy**.
6. **Data Catalog**: Enabled schema updates and partitioning for target table `ticker_demo_parquet`.
7. **IAM Role**: Created a custom IAM role with the following permissions:
   - `AmazonS3FullAccess`
   - `AWSGlueServiceRole`
8. **Job Configuration**:
   - Type: Spark
   - Version: Latest Glue version
   - Language: Python 3
   - Worker Type: G 1X
   - Number of Workers: 2
9. **Execution**: Ran the job and validated the output Parquet files using **S3 Select** and verified their format and compression.
![image](https://github.com/user-attachments/assets/8fa96187-6429-4545-9c9f-e3e6bfb5191b)

![image](https://github.com/user-attachments/assets/4a36a1d9-64e6-4d05-b47f-f3f13ca6a2c7)

## ✅ Outcome

- Successfully created a new Parquet-format dataset in S3.
- Verified schema and data correctness using S3 Select with Apache Parquet format.

---
