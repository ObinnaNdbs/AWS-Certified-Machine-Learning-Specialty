# 🔍 Amazon Kendra Hands-On Lab

This lab demonstrates how to use **Amazon Kendra** for intelligent search by indexing documents stored in an **Amazon S3 bucket**.

---

## 🛠️ Lab Overview

**Objective**:  
Use Amazon Kendra to index documents from an S3 bucket and enable natural language search over the content.

---

## 🧪 Steps Performed

1. **Created an S3 Bucket**
   - Bucket name: `kendra-related-info`
   - Uploaded two folders:
     - `/html/` – HTML files
     - `/pdf/` – PDF files
![image](https://github.com/user-attachments/assets/be827017-23c8-4f6e-93e5-55ce674fa008)

2. **Created an Amazon Kendra Index**
   - Chose *Developer Edition* for cost-effectiveness
   - Created an IAM role automatically during setup
![image](https://github.com/user-attachments/assets/0f5cb305-835d-41c4-9aaa-66cee03b825f)

3. **Connected S3 as a Data Source**
   - Named data source: `demo-data-set-s3`
   - Used the Kendra connector to sync S3 content with the index
![image](https://github.com/user-attachments/assets/5971f2bf-b962-44ca-aa1c-5578a0ffab07)

4. **Executed a Search Query**
   - Example: `"aws deep learning ami"`
   - Kendra retrieved and ranked relevant answers from the uploaded documents
![image](https://github.com/user-attachments/assets/b5d88c2f-204a-452a-ae87-4c79af29cad3)

---

## ✅ Outcome

Successfully tested Amazon Kendra's ability to:
- Index structured documents from S3
- Understand and retrieve answers using natural language queries

---
