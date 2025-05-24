# 🧪 Exploratory Data Analysis (EDA)

This module covers the tools and techniques necessary to prepare, visualize, and understand data prior to modeling. Emphasis is placed on AWS-native services (e.g., SageMaker Ground Truth, Athena, QuickSight, EMR), along with essential data analysis and feature engineering skills.
![image](https://github.com/user-attachments/assets/6cb64f42-781b-4108-b5d1-658ea18930e2)

---

## 🔍 Core Topics Covered

### 📂 Data Understanding & Profiling
- Types of data (numerical, categorical, text, image)
- Data distribution and descriptive statistics
- Detecting and handling missing values
- Identifying and managing outliers
- Understanding unbalanced datasets

<!-- Optional Image -->
<!-- ![Example of Data Distribution](../assets/data_distribution_plot.png) -->

---

### 🔄 Data Transformation
- Scaling (standardization, normalization)
- One-hot encoding and binning
- Text & image preprocessing techniques
- TF-IDF vectorization with Spark on EMR
- Dimensionality reduction (PCA)

<!-- Optional Image -->
<!-- ![TF-IDF Vectorization](../assets/tfidf_pipeline.png) -->

---

### 🛠️ Feature Engineering
- Extracting features from raw data
- Handling curse of dimensionality
- Creating new features (synthetic variables)
- Engineering time-series data (seasonality & trends)

---

### 📊 Visualization & Interpretation
- Types of visualizations and when to use them
- Time-series trend analysis
- Visualizing distributions, correlations, and clusters

<!-- Optional Image -->
<!-- ![Visualization Example](../assets/quicksight_dashboard.png) -->

---

## ☁️ AWS Tools Used

- **Amazon SageMaker Ground Truth** – Manual labeling for supervised learning datasets
  - [HOL] Create a labeling job
    
![image](https://github.com/user-attachments/assets/75d102bf-d2d1-4a21-a373-94533edadd19)

- **Amazon Athena** – Querying data using SQL
  - [HOL] Run SQL queries on Athena
![image](https://github.com/user-attachments/assets/e8e8a6c2-5a3c-48be-b581-d1f8d03cc2d5)

- **Amazon QuickSight** – Visualize trends and feature patterns
  - [HOL] Create QuickSight analysis
![image](https://github.com/user-attachments/assets/1a768274-f1ac-467b-b9da-bd3fcce0bbfb)

- **Amazon EMR (Apache Spark)** – Distributed EDA at scale
  - [Lab] Preparing TF-IDF with Spark + EMR Studio (Part 1 & 2)
![image](https://github.com/user-attachments/assets/b2427628-7434-42a8-a9ca-064563907af9)

- **Jupyter Notebooks (SageMaker Studio)** – In-notebook analysis
![image](https://github.com/user-attachments/assets/4beff8e6-cd45-44c1-9332-7bc16a86a2d4)

- **CRISP-DM** – Framework for managing the EDA process

---

## ✅ Hands-On Labs
> Include screenshots or summaries of lab outcomes if showcasing for a project portfolio

- [x] TF-IDF with Spark on EMR
- [x] Athena SQL Queries
- [x] Amazon QuickSight Analysis
- [x] SageMaker Ground Truth Labeling Job

---

## 📚 Related Concepts

- CRISP-DM process (underpinning ML workflows)
- Data exploration as input to feature engineering and model tuning
- The role of EDA in ML pipelines and production readiness

---

