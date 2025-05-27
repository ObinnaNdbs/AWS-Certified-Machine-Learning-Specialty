# 🧠 Sentiment Analysis Pipeline using Amazon Comprehend, Athena, Glue, and QuickSight

This project implements a full end-to-end sentiment analysis workflow on customer reviews using Amazon's cloud-native AI and analytics tools. It showcases how raw textual data can be transformed into insights using a serverless architecture.

---

## 🎯 Objective

Analyze the sentiment (Positive, Negative, Neutral, Mixed) of customer reviews stored in an S3 bucket and present the results visually in a pie chart using Amazon QuickSight.

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

### 2. **Sentiment Analysis (Amazon Comprehend)**
- Created a *Sentiment Analysis Job* in Comprehend:
  - Input: CSV file (1 line per document)
  - Output: S3 directory
  - IAM Role created with input/output permissions to S3

### 3. **Preprocessing the Output**
- Unzipped and re-uploaded the output file to a new S3 folder (`sentiment-output-uncompressed/`).

### 4. **Schema Extraction (AWS Glue)**
- Created a Glue Crawler (`Sentiment Crawler`) to:
  - Identify JSON schema of the uncompressed Comprehend output
  - Create a Glue Catalog Table with columns: `file`, `line`, `sentiment`, `sentimentScore`

### 5. **Data Querying (Amazon Athena)**
- Queried the Glue Catalog table using Athena to:
  - Extract each sentiment category score (Positive, Negative, Neutral, Mixed)
  - Save query output as a new table: `sentiment_results_final`

### 6. **Visualization (Amazon QuickSight)**
- Connected QuickSight to Athena and imported the final table
- Used Autograph and Pie Chart to visualize:
  - % of positive reviews
  - % of negative reviews
  - % of mixed and neutral reviews

> Example Output: Pie Chart  
> ✅ 93% Positive  
> ❗️ 3% Mixed  
> ❗️ 3% Negative

---


---

## 💡 Key Learning Outcomes

- How to launch and monitor a **sentiment analysis job** using Amazon Comprehend
- How to configure **IAM roles** and S3 input/output permissions
- How to use **AWS Glue Crawlers** to dynamically infer data schemas
- How to transform and **query JSON data with SQL** in Amazon Athena
- How to create an **interactive visualization dashboard** in QuickSight

---

## 📷 Suggested Visuals to Include (Optional)

- Screenshot of the input CSV in S3
- Comprehend job creation page
- Glue Crawler run summary
- Athena SQL results table
- Final QuickSight pie chart

---

## ✅ Status: Completed (Deployed using Console)


