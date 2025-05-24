# Lab: Creating an Amazon SageMaker Notebook Instance

This lab walks through the process of launching a basic Amazon SageMaker notebook instance from the AWS Console. The goal is to familiarize yourself with the setup process and explore built-in SageMaker examples for training and hosting machine learning models.
![image](https://github.com/user-attachments/assets/aea18857-abf2-4370-a23c-a62ffa36d9a0)

---

## ✅ Steps Completed

1. **Opened the AWS Console** and navigated to **Amazon SageMaker**.
2. **Created a new notebook instance**:
   - **Name**: `demo-notebook`
   - **Instance Type**: `t2.medium`
   - **Volume Size**: Default (5 GB)
   - **Elastic Inference**: Not used
   - **IAM Role**: Selected as required
   - **VPC Configuration**: Not used (left default for simplicity)
![image](https://github.com/user-attachments/assets/bac7e0b0-29e7-4555-be8b-5bf4b69a3a31)

3. **Started the notebook instance** and waited for it to reach `InService` state.
4. **Opened Jupyter Notebook** from the instance dashboard.
![image](https://github.com/user-attachments/assets/2f79f54d-a46d-4dca-a098-35867a7e3a61)

5. **Explored built-in SageMaker examples**:
   - Loaded **Breast Cancer Prediction** notebook (Python Interactive Notebook).
   - Observed:
     - Library imports
     - Data upload to S3
     - Training and hosting workflow structure
![image](https://github.com/user-attachments/assets/d13682e0-1775-4377-ad7e-a3347f4894e7)

---

## 🛠️ Tools & Skills Demonstrated

- SageMaker Notebook instance creation
- Understanding of instance types and configurations
- Navigating Jupyter in SageMaker
- Loading and using built-in example notebooks
- Initial exposure to data ingestion, training, and hosting flow in SageMaker

---
