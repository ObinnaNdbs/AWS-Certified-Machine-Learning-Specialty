# Lab: AWS Glue Crawler – Creating a Table from S3 Data

In this lab, we configured an AWS Glue Crawler to scan an S3 bucket, extract metadata, and populate a table in the Glue Data Catalog.

## 🔧 Steps Performed

1. **Opened Glue Console** → Navigated to **Crawlers** under **Data Catalog**
2. **Created Crawler** named `DemoCrawler`
3. **Selected Data Source** as:
   - Location: Amazon S3
   - Bucket: `machine_learning_course`
   - Crawled all sub-folders
4. **Configured IAM Role** named `DemoGlueCrawlerS3` with:
   - `GlueServiceRole` permissions
   - `S3 GetObject` and `PutObject` access to the target bucket
  ![image](https://github.com/user-attachments/assets/a7ff6704-41ef-49c2-a433-b60794be4ab3)

5. **Created Glue Database** called `machine_learning`
6. **Set Crawler Output**:
   - Target: `machine_learning` database
   - No table prefix or scheduling (on-demand run)
7. **Ran the Crawler** to populate the Data Catalog
 ![image](https://github.com/user-attachments/assets/8a0265eb-81f1-49d1-9ac7-082d54b818d0)

8. **Verified Results**:
   - One table and partition created
   - Inferred schema: `change`, `price`, `ticker_symbol`, `sector`
   - Partitions: `year`, `month`, `day`, `hour`

![image](https://github.com/user-attachments/assets/c0d33bde-759f-41e2-b92f-170c2391db70)

## ✅ Outcome

- A Glue table was automatically generated from partitioned JSON files stored in S3.
- Table schema and partitions were inferred successfully.

---
