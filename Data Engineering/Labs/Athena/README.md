# Lab: Querying Data in Amazon Athena

In this lab, we practiced using **Amazon Athena** to instantly query data stored in **Amazon S3** using SQL. Athena connects to the **AWS Glue Data Catalog**, allowing us to run SQL queries on structured datasets.
![image](https://github.com/user-attachments/assets/3225cd7b-3904-4bc4-a685-3e6e162ce6b4)

## 🔧 Steps Performed

1. **Configured Query Result Location**:
   - Set the output location in S3:  
     `s3://<your-bucket-name>/athena_results/`

2. **Navigated the Athena Query Editor**:
   - Connected Athena to the Glue Data Catalog.
   - Selected the `machine_learning` database.
   - Identified the table `ticker_demo_parquet`.
![image](https://github.com/user-attachments/assets/78810e91-f728-4054-901a-3182d8bbbb19)

3. **Ran SQL Queries**:
   - Used the default preview feature, which executed:  
     ```sql
     SELECT * FROM "machine_learning"."ticker_demo_parquet"
     ```
![image](https://github.com/user-attachments/assets/a4561845-c126-494f-9517-852e59baa85b)

4. **Observed Output**:
   - Viewed tabular data such as `change`, `price`, `ticker symbol`, and `sector`.
   - Validated Athena’s ability to read JSON-based tables as well.

## ✅ Outcome

- Successfully previewed two tables using Athena.
- Verified seamless SQL-based querying from S3 data.
- Demonstrated integration between Athena and the Glue Data Catalog.

---
