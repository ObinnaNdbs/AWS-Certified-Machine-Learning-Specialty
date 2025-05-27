# 🧠 Sentiment Analysis Pipeline using Amazon Comprehend, Athena, Glue, and QuickSight

This project implements a full end-to-end sentiment analysis workflow on customer reviews using Amazon's cloud-native AI and analytics tools. It showcases how raw textual data can be transformed into insights using a serverless architecture.

---

## 🎯 Objective

Analyze the sentiment (Positive, Negative, Neutral, Mixed) of customer reviews stored in an S3 bucket and present the results visually in a pie chart using Amazon QuickSight.
![image](https://github.com/user-attachments/assets/558f862a-5198-42f8-b790-aea1e1a4b7df)

---

## 🛠️ Tools & AWS Services Used

| Service              | Purpose                                                       |
|----------------------|---------------------------------------------------------------|
| **Amazon S3**        | Storage for input CSV and all intermediate/output artifacts   |
| **Amazon Comprehend**| Sentiment analysis using NLP                                  |
| **AWS Glue**         | Schema extraction using Glue Crawlers, catalog creation       |
| **Amazon Athena**    | SQL-based data transformation and filtering                   |
| **Amazon QuickSight**| Dashboard and pie chart generation for visualization          |

---

## 🗂️ Project Workflow

### 1. **Data Preparation (Amazon S3)**
- Uploaded a CSV file of customer reviews to a new S3 bucket.
- Each row in the file represents a user review (1 sentence per line).
![image](https://github.com/user-attachments/assets/bd393904-ff3f-4859-b32d-50430081bf51)
![image](https://github.com/user-attachments/assets/d61ba894-0ccf-4059-9d92-96d6ac9378ba)

### 2. **Sentiment Analysis (Amazon Comprehend)**
- Created a *Sentiment Analysis Job* in Comprehend:
  - Input: CSV file (1 line per document)
  - Output: S3 directory
  - IAM Role created with input/output permissions to S3
![image](https://github.com/user-attachments/assets/a4b502a3-9ad7-4c99-b0e5-4abc10f88fe1)

![image](https://github.com/user-attachments/assets/374425c9-92b2-4576-a7de-eb0b81e1c800)

### 3. **Preprocessing the Output**
- Unzipped and re-uploaded the output file to a new S3 folder (`sentiment-output-uncompressed/`).
![image](https://github.com/user-attachments/assets/4a7af2ca-ff67-4926-aa63-249fb9bacf1a)
![image](https://github.com/user-attachments/assets/4700c6c1-55f1-41f3-947b-fda9d64950f8)

### 4. **Schema Extraction (AWS Glue)**
- Created a Glue Crawler (`Sentiment Crawler`) to:
  - Identify JSON schema of the uncompressed Comprehend output
  - Create a Glue Catalog Table with columns: `file`, `line`, `sentiment`, `sentimentScore`
![image](https://github.com/user-attachments/assets/f22082d5-606a-43af-bca9-f6f7460e428c)
![image](https://github.com/user-attachments/assets/aa4f2e5b-c0af-443b-b0ec-6b1eec46d07b)
![image](https://github.com/user-attachments/assets/914efd45-721c-489d-b1f0-85e93da3633a)
![image](https://github.com/user-attachments/assets/741364d9-70e9-44ff-a0ec-a1baa0a6636c)

### 5. **Data Querying (Amazon Athena)**
- Queried the Glue Catalog table using Athena to:
  - Extract each sentiment category score (Positive, Negative, Neutral, Mixed)
  - Save query output as a new table: `sentiment_results_final`
![image](https://github.com/user-attachments/assets/37357673-5ec0-44ab-87b2-98c82a710558)

### 6. **Visualization (Amazon QuickSight)**
- Connected QuickSight to Athena and imported the final table
- Used Autograph and Pie Chart to visualize:
  - % of positive reviews
  - % of negative reviews
  - % of mixed and neutral reviews

![image](https://github.com/user-attachments/assets/d2d6285c-61cc-4f42-b4b8-8ff065e8c361)

> Example Output:  
![image](https://github.com/user-attachments/assets/14bbbd07-e4dc-44ef-8064-13edeef4a9f9)
![image](https://github.com/user-attachments/assets/34f3fbf7-1578-4e1e-970e-6da0adc03500)

---

## 💡 Key Learning Outcomes

- How to launch and monitor a **sentiment analysis job** using Amazon Comprehend
- How to configure **IAM roles** and S3 input/output permissions
- How to use **AWS Glue Crawlers** to dynamically infer data schemas
- How to transform and **query JSON data with SQL** in Amazon Athena
- How to create an **interactive visualization dashboard** in QuickSight

---

## ✅ Status: Completed (Deployed using Console)


