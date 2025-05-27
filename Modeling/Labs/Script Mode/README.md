# 📜 SageMaker Script Mode Lab

This lab demonstrates how to train and deploy a machine learning model in **Amazon SageMaker** using **Script Mode** with the managed **Scikit-Learn** container.

---

## 🧪 Lab Summary

In this hands-on lab, we explored one of SageMaker’s flexible training options—Script Mode—where you use **your own Python training script** inside a **prebuilt AWS-managed container** (e.g., `sklearn`). This is a practical middle ground between using built-in algorithms and fully custom containers.

---

## ✅ What We Did

- Navigated to **Amazon SageMaker > Notebook instances**
- Opened an existing notebook via **Jupyter**
- Located the sample: `sagemaker-script-mode/sklearn_byo` and created a copy
- Executed steps to:
  - Download and prepare data
  - Split into training and validation sets
  - Define a **Scikit-Learn Estimator** using `train.py` as the entry point
  - Set `script_mode=True` to use our custom script
  - Train and deploy the model to a SageMaker endpoint
  - Test the deployed model
![image](https://github.com/user-attachments/assets/31c99d8f-e16a-4538-9307-e70bb1998ef4)

---

## 💻 Key Components

- `train.py`: Your custom training script (entry point)
- `SKLearn` Estimator:
  - Specifies script path
  - Uses AWS managed `scikit-learn` container
- SageMaker endpoint deployment

---

## 🧰 Skills Demonstrated

- Script Mode training in SageMaker
- Using AWS-managed containers
- Passing your own training logic via Python script
- Model deployment and testing

---


