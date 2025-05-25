# 🧪 Lab: Regression Modeling in SageMaker Canvas (California Housing)

This lab demonstrates how to build a **regression model** in **Amazon SageMaker Canvas** using the California Housing dataset. The goal is to predict **median house value** based on various housing features using a low-code/no-code interface.

---

## 🔧 Steps Performed

### 1. **Upload Dataset to S3**
- Dataset: *California Housing*
- Uploaded to: `S3 > dct-bucket-demo/housing/`
- Format: CSV
![image](https://github.com/user-attachments/assets/46ce7320-1932-442e-941b-1445fe3f0c06)

### 2. **Import into SageMaker Canvas**
- Opened SageMaker Canvas from the AWS Console
![image](https://github.com/user-attachments/assets/553ccb42-6c6a-4941-84a6-afdac4c60e9a)

- Imported the dataset via:
  - **Data Source**: Amazon S3
  - **Data Type**: Tabular
  - **Target Column**: `median_house_value`

### 3. **Data Exploration & Preprocessing**
- Explored column-wise statistics: missing values, standard deviation, data distribution
- Applied transformations:
  - Replaced missing values (manual: median imputation for `total_bedrooms`)
  - Viewed correlations (e.g., strong between `total_rooms` and `total_bedrooms`)
  - Visualized features using scatter plots and box plots
  - Built transformation recipes (e.g., rename column, drop column)
![image](https://github.com/user-attachments/assets/691000cc-6bec-434c-8821-8a521053c890)
![image](https://github.com/user-attachments/assets/ceabf41f-365b-4812-a6b3-9564a1c8f76a)
  
### 4. **Model Building**
- Model Type: Predictive Analysis (Regression)
- Build Option: **Quick Build** (fast, less accurate)
- Evaluated:
  - RMSE, MAE, Residual plots
  - Feature importance: `longitude` and `latitude` were most influential
![image](https://github.com/user-attachments/assets/33a6c32c-3ea3-454c-a7fc-817a16041f01)

### 5. **Prediction**
- Single prediction based on custom input values
- Option to export predictions (CSV/image)
- Noted: Option to perform **batch predictions** using datasets
![image](https://github.com/user-attachments/assets/3f703679-9f67-4be2-90b5-e3332d476ca0)

---

## 🛑 Cleanup
- Manually logged out of SageMaker Canvas to avoid unnecessary billing.

---

## ✅ Key Skills & Tools Used
- Amazon SageMaker Canvas
- S3 for data storage
- No-code ML modeling
- Data wrangling & imputation
- Regression metrics evaluation (RMSE, residuals)
- Feature importance analysis
- Basic EDA with graphs

---

