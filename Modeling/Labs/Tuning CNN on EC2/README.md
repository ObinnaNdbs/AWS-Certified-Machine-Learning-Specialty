# 🧪 Lab: Tuning a Convolutional Neural Network on EC2 (Parts 1–3)

This lab series explores hands-on training, tuning, and optimization of a convolutional neural network (CNN) using **TensorFlow + Keras** on a self-managed **EC2 GPU instance**. Instead of SageMaker, we used an AMI-based setup to simulate a real-world deployment experience, emphasizing manual setup, configuration, and cost-awareness.

---

## 🧱 Part 1: Environment Setup and Jupyter Notebook Launch

- Launched a **Deep Learning AMI with GPU (Ubuntu 20.04)** for TensorFlow on a `p3.2xlarge` instance.
- Used **PuTTY** to SSH into the EC2 instance and forward **port 8888** to access the Jupyter Notebook server.
- Uploaded and opened the provided notebook `Keras-CNN-Tuning.ipynb`.
- Objective: Experience manual EC2 setup and Jupyter tunnel for custom training environments.
![image](https://github.com/user-attachments/assets/44a53868-68e8-46d0-a35d-0a6f3796eb6f)
![image](https://github.com/user-attachments/assets/7afb874a-44cd-489f-8dfb-1abb1fb741e7)
![image](https://github.com/user-attachments/assets/ffd6400a-cf68-4397-83c9-f29b2ef1be3a)

---

## 🧠 Part 2: Building and Training the CNN

- Loaded and preprocessed the **MNIST** dataset:
  - Reshaped images to (28×28)
  - Normalized pixel values to [0, 1]
  - One-hot encoded the labels
- Built a CNN with:
  - Two Conv2D layers → MaxPooling → Flatten → Dense → Softmax
- Trained over 10 epochs with:
  - `batch_size = 32`
  - `optimizer = Adam`
  - `loss = categorical_crossentropy`
  - Evaluated training vs. validation accuracy

### Observations:
- **Overfitting** detected: training accuracy exceeded validation accuracy.
- Motivated need for **regularization** techniques.

---

## 🔧 Part 3: Regularization and Hyperparameter Tuning

- Introduced **Dropout layers** after Conv and Dense layers to prevent overfitting.
- Re-trained the model, resulting in:
  - **Improved validation accuracy** (~99.23% vs 99.07%)
  - Training and validation accuracies more aligned → better generalization

### Hyperparameter Experiments:
- **Batch Size**: Increased to 1000 → model underperformed due to local minima
- **Learning Rate**: Increased to 0.01 → model failed to converge properly
  - Conclusion: small learning rate + batch size = better convergence
![image](https://github.com/user-attachments/assets/d3c0f656-df6d-4654-a25d-de2e564eb8bd)
- Terminate when done to prevent charges
![image](https://github.com/user-attachments/assets/e5632c88-9121-4c02-88d0-ccac81b3a9db)

---

## ✅ Key Concepts Practiced

- Setting up GPU-enabled EC2 environments
- Tunneling Jupyter Notebooks securely via PuTTY
- Data preprocessing for deep learning
- Building and training CNNs with Keras
- Overfitting detection and mitigation via dropout
- Hyperparameter tuning: batch size and learning rate effects
- Manual EC2 cleanup to avoid billing charges

---


📌 **NOTE**: This hands-on lab is important for the MLS-C01 exam, which emphasizes **real-world model tuning experience**, not just theory.
