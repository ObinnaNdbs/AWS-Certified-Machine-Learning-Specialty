# TF-IDF Wikipedia Search Engine with PySpark on AWS EMR Studio

## 🧠 Project Summary
This project demonstrates how to build a scalable, distributed text processing pipeline using **Apache Spark** and **AWS EMR Studio** to compute **TF-IDF (Term Frequency – Inverse Document Frequency)** scores on a subset of Wikipedia articles. It culminates in a lightweight search engine that ranks documents based on relevance to a given term.

---

## ⚙️ Tools & Technologies
- **Apache Spark (PySpark)**: Used for distributed processing and MLlib transformations.
- **AWS EMR Studio (Serverless)**: Used to create interactive Jupyter notebooks for Spark jobs.
- **Amazon S3**: Data source and notebook storage.
- **Spark MLlib**: Tokenizer, HashingTF, IDF, and UDFs for extracting TF-IDF values.
- **Wikipedia Subset Dataset**: Small `.tsv` file containing article titles and content.

---

## 🔁 Pipeline Overview
1. **Load Data**: Read Wikipedia subset from S3 using Spark.
![image](https://github.com/user-attachments/assets/356deeb2-3edc-40b2-8605-bb41fe9d1e8c)
![image](https://github.com/user-attachments/assets/c5aa5e8e-ed64-4275-87cc-af3b137e4f27)

2. **Preprocessing**: Drop nulls, lowercase text, tokenize articles.
![image](https://github.com/user-attachments/assets/82cacb3e-f2cc-4b6a-869c-a2e76e367920)

3. **Feature Engineering**:
   - Apply `Tokenizer` to split documents into words.
   - Use `HashingTF` to compute term frequencies.
   - Use `IDF` to compute inverse document frequencies.
![image](https://github.com/user-attachments/assets/6028785a-906f-4470-8040-bca3dd64ccdf)

4. **TF-IDF Scoring**:
   - Compute the TF-IDF matrix for the corpus.
   - Extract scores for a search term (e.g., “Gettysburg”) using hashing.
   - Rank and display the most relevant articles based on TF-IDF.
![image](https://github.com/user-attachments/assets/92747bf2-c10d-4b6a-b20b-dca4d4b3a9a9)

---

## ✅ Skills Demonstrated
- Scalable data preprocessing using Spark
- Building custom NLP pipelines
- Feature extraction using TF-IDF
- Working with EMR Studio, EMR Serverless, and S3
- Cleaning and transforming large text datasets
- Data analysis using Spark DataFrames

---

## 🔎 Sample Use Case
Searching for the term `Gettysburg` successfully returns:
- **Abraham Lincoln**
- **American Civil War**
- **Abner Doubleday**

Demonstrating how TF-IDF can identify document relevance in a distributed setting.

---

## 🧹 Cleanup Checklist
Ensure the following AWS resources are deleted after use:
- EMR Serverless Application
- EMR Workspace & Studio
- Any large datasets in S3

---

## 🏁 Status
✅ Completed — Ready for inclusion in resume and GitHub portfolio.
