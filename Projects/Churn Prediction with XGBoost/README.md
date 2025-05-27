# XGBoost Customer Churn Prediction with Amazon SageMaker

This project demonstrates a full pipeline for predicting customer churn using the **XGBoost** algorithm on **Amazon SageMaker**. It includes data preprocessing, exploratory data analysis (EDA), model training, hyperparameter tuning, deployment, and inference through a live endpoint.

## 🛠️ Tools & Services Used
- Amazon SageMaker (Training, Deployment, Endpoint Hosting)
- Amazon S3 (Data storage)
- Boto3 (AWS SDK for Python)
- Pandas & NumPy (Data preprocessing and manipulation)
- XGBoost (Machine learning model)
- Python SDK for SageMaker

---

## 📁 Files Included
- `xgboost_customer_churn.ipynb`:  
  Full pipeline covering EDA, data preprocessing, model training, and hyperparameter tuning.

- `xgboost_customer_churn_outputs.ipynb`:  
  Notebook for model deployment, endpoint creation, inference (prediction), and basic model evaluation.

---

## 🧪 Steps Performed

### 1. Data Exploration & Preprocessing
- Dataset: 5,000 customer records, 21 columns (20 features + 1 target).
- Dropped irrelevant features like `phone number` (unique identifier).
- Removed highly correlated features (e.g., `day minutes` vs. `day charge`).
- Converted categorical variables into numerical format.
- Split data into training, validation, and testing sets.
- Saved and uploaded datasets to Amazon S3.

### 2. Model Training with XGBoost on SageMaker
- Fetched the latest XGBoost container from AWS.
- Defined an `Estimator` object with hyperparameters:
  - `max_depth=5`
  - `eta=0.2`
  - `objective='binary:logistic'`
- Trained the model using the training and validation datasets stored in S3.

### 3. Model Deployment & Inference
- Deployed the trained model to a real-time SageMaker endpoint.
- Used `predictor.predict()` to make predictions on new data.
- Performed basic model evaluation using predictions and labels.

---

## ✅ What You Can See in the Notebooks
- Setup of AWS environment using SageMaker roles and sessions.
- Use of SageMaker's high-level Estimator API.
- Step-by-step model training and deployment process.
- Live inference with deployed endpoint.
- Output from SageMaker console (via logs) during training and deployment.

---

## 🔒 Note
Make sure to shut down the deployed endpoint via `predictor.delete_endpoint()` to avoid ongoing charges.

---

