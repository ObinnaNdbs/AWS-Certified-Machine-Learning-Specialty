# 📊 SageMaker Data Wrangler Lab – Hotel Booking Dataset

This lab demonstrates the use of **Amazon SageMaker Data Wrangler** for preparing and transforming a dataset for machine learning workflows. We explored basic feature analysis, data quality inspection, visualizations, and applied common data transformations using the **Hotel Booking Demand Dataset** (from Kaggle).

---

## 🧰 Tools Used

- **Amazon S3** – For storing and importing the dataset
- **Amazon SageMaker Studio** – Main interface for launching Data Wrangler
- **SageMaker Data Wrangler** – For preprocessing, analysis, and feature engineering

---

## 📂 Dataset Overview

- **Source**: Hotel Booking Demand (CSV format)
- **Target Column**: `is_canceled` (binary classification: 0 = not canceled, 1 = canceled)

---

## ✅ Steps Performed

### 1. Data Import & Setup
- Uploaded dataset to S3 under a new folder `bookings`
- Created a new Data Wrangler flow named `bookings`
- Imported the dataset using the first 50,000 rows as a sample
![image](https://github.com/user-attachments/assets/ccda4b93-b95d-4939-a60e-db9eeb741055)

### 2. Exploratory Analysis
- **Data preview and type detection**
- **Data Quality and Insights Report**:
  - Detected 30% duplicate rows
  - Detected **target leakage** from columns like `reservation_status`
  - Evaluated class balance in the target variable
  - Reviewed anomalous samples and feature importance
![image](https://github.com/user-attachments/assets/6f69f764-8e26-4367-b806-09cfe0d3735c)
![image](https://github.com/user-attachments/assets/46eb05f8-3baf-49fd-97ea-b9bce453389e)

### 3. Data Visualizations
- Created a **histogram** for `is_canceled`
- Created a **scatter plot** between `lead_time` and `ADR`
- Ran a **duplicate rows analysis** to quantify data repetition
![image](https://github.com/user-attachments/assets/d650b0cb-cc45-4fe4-9d57-1b6422de4926)
![image](https://github.com/user-attachments/assets/2d4f23a6-47fa-43f4-b90b-72de84c69451)

### 4. Data Transformations
- 🧹 **Dropped duplicate rows**
- 🧮 **Handled missing values**: Filled missing values in `children` with 0
- 🚫 **Detected outliers** in `lead_time` using ±4 standard deviations
![image](https://github.com/user-attachments/assets/acf8c997-b8d7-43b8-858c-598b5263ebbf)

---

## 🧼 Resource Cleanup
- Shut down SageMaker Studio kernel
- Deleted the SageMaker domain and associated user profile to prevent ongoing charges

---
