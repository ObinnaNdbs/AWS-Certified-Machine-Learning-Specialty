# 🧠 Mammographic Mass Classification with Deep Learning

## Overview

This project applies a **Multi-Layer Perceptron (MLP)** using **Keras/TensorFlow** to classify mammographic masses as **benign** or **malignant**. The dataset used comes from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Mammographic+Mass), containing medical imaging data from mammograms.

### 🔍 Objective

To build a supervised deep learning model that:
- Cleans and prepares the data.
- Encodes categorical variables.
- Normalizes continuous variables.
- Trains and evaluates a neural network.
- Achieves high accuracy in classifying cancerous vs. non-cancerous masses.

---

## 📊 Dataset Details

**Filename:** `mammographic_masses.data.txt`  
**Instances:** 961  
**Features:**
- `BI-RADS` (assessment score; dropped for modeling)
- `Age` (continuous)
- `Shape` (categorical: 1=round, 2=oval, 3=lobular, 4=irregular)
- `Margin` (categorical: 1=circumscribed, 2=microlobulated, 3=obscured, 4=ill-defined, 5=spiculated)
- `Density` (ordinal: 1=high, 2=iso, 3=low, 4=fat-containing)
- `Severity` (target: 0=benign, 1=malignant)

---

## 🧹 Data Preprocessing

- Missing values (`?`) were handled using `na_values` and `dropna()`.
- Columns were labeled using:
  ```python
  ['BI-RADS', 'age', 'shape', 'margin', 'density', 'severity']
  ```
  - **BI-RADS** was removed from the dataset as it's not a predictive feature.
- Features were cast to numerical types and scaled using `MinMaxScaler` for neural network compatibility.

---

## 🧠 Model Architecture

A **Multi-Layer Perceptron (MLP)** was created using the Keras `Sequential` API:

```python
model = Sequential()
model.add(Dense(10, activation='relu', input_shape=(4,)))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
```

## ⚙️ Model Configuration

- **Optimizer:** Adam  
- **Loss Function:** Binary Crossentropy  
- **Metric:** Accuracy  
- **Epochs:** 100  
- **Batch Size:** 10  

---

## 📈 Evaluation

- Model was trained with an **80/20 train-test split**.
- **Accuracy exceeded 80%**, matching or beating baseline expectations.
- Performance was visualized using `matplotlib` to show:
  - Loss curve over epochs
  - Accuracy curve over epochs

---

## 🧪 How to Run

1. **Install dependencies**:

    ```bash
    pip install pandas numpy scikit-learn matplotlib tensorflow
    ```

2. **Ensure the dataset** `mammographic_masses.data.txt` **is present in the working directory.**

3. **Run the notebook**:

    ```bash
    jupyter notebook DeepLearningProject-Solution.ipynb
    ```

---

## ✅ Results Summary

- Clean and well-prepared medical dataset.
- Simple yet effective MLP implementation.
- Achieved competitive classification accuracy with low computational cost.
- Demonstrated practical application of neural networks in medical diagnostics.

---

## 📚 References

- [UCI Mammographic Mass Dataset](https://archive.ics.uci.edu/ml/datasets/Mammographic+Mass)
- [TensorFlow Documentation](https://www.tensorflow.org/)
- [HuggingFace Transformers](https://huggingface.co/transformers/)


---
