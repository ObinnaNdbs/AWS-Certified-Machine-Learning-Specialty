# Lab: Data Cleaning and Transformation with AWS Glue DataBrew

## Overview
In this lab, we explored AWS Glue DataBrew, a visual data preparation tool used to clean and normalize data without writing code. The key goal was to understand how to use DataBrew to apply data transformations and create reusable workflows via "recipes".

## Steps Performed

1. **Created a DataBrew Project** named `demo project`.
2. **Connected a Dataset** from the AWS Glue Data Catalog.
   - Dataset: `ticker_demo` (Parquet format)
   - Source: S3 via the Data Catalog
3. **Created an IAM Role** for DataBrew to access the data.
   ![image](https://github.com/user-attachments/assets/e81b5187-9fba-45e2-b3c5-738f8cfecfe6)

5. **Explored the Dataset:**
   - Viewed sample rows and statistical summaries
   - Identified data distribution, min, max, mean, standard deviation, etc.
6. **Applied a Transformation:**
   - Used a Math function: `floor()` on the `price` column
   - Created a new column: `price_floor`
7. **Reviewed the Recipe:**
   - The transformation step was saved to the recipe for reuse.
  ![image](https://github.com/user-attachments/assets/ba3dde34-7722-4404-8cfe-8e763f0d65be)

8. **Created and Ran a Job:**
   - Output format: CSV
   - Destination: Amazon S3 (`ticker_demo_DataBrew`)
   - Verified the output via **S3 Select**
![image](https://github.com/user-attachments/assets/51ba493d-dc3f-4f53-9998-c55b6fc6cd94)

## Output
- Cleaned dataset with a new column (`price_floor`)
- CSV files stored in S3
- Transformation job ran successfully and validated

