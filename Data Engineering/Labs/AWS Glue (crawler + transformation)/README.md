# AWS Glue Lab: Crawler + Transformation

## 🧪 Overview
This lab demonstrates how to use AWS Glue to:
- Automatically extract schema from a CSV file using a **Glue Crawler**
- Apply a basic **schema transformation** using a **Glue Job**

## 📂 Data Source
- File: `players.csv` (sample file)
- Location: `s3://DCT-bucket-demo/`
- Structure: `id`, `name`, `age`, ..., `release_clause`

## Steps Performed

### 1. 📥 **Crawler Creation**
- Created a Glue Crawler named `crawler_demo`
- Set S3 data source path to: `s3://DCT-bucket-demo/`
- IAM Role: Pre-existing Glue service role with S3 access
- Created a Glue database: `players`
- Ran the crawler → Extracted schema into a table within the `players` database
![image](https://github.com/user-attachments/assets/a4999b19-e8ba-43ea-bfb7-d9b50065573e)

### 2. 🧪 **Glue Job: Schema Transformation**
- Job Name: `glue_job`
- IAM Role: Same as crawler
- Type: Spark job (auto-generated script by AWS Glue)
  ![image](https://github.com/user-attachments/assets/349b1175-82ed-4a1c-9a52-4974a904e6ff)

- Input Source: `players` database table
- Transformation: Renamed column `id` → `number`
- Target Location: `s3://DCT-bucket-demo/`
- Output File: Modified CSV with renamed column
![image](https://github.com/user-attachments/assets/65d24f43-feb2-44e8-a737-a14f0438f68e)

## ✅ Outcome
- Original schema auto-detected by crawler
- Column `id` renamed to `number` using transformation job
- Transformed file saved back to same S3 bucket
![image](https://github.com/user-attachments/assets/704dbf40-5f18-4f4d-ab29-902ac9653e8a)

---

