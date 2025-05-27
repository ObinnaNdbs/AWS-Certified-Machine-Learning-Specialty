# Lab: Deploying and Tuning a Custom TensorFlow Model with SageMaker

In this lab, we built on a pre-trained Convolutional Neural Network (CNN) for digit recognition using the MNIST dataset and deployed it using Amazon SageMaker. We also experimented with Elastic Inference and conducted hyperparameter tuning using SageMaker’s built-in tuning capabilities.

## 🔧 What We Did

### ✅ Step 1: Model Training on GPU
- Trained a TensorFlow-based CNN using a `p3.2xlarge` GPU instance.
- Dataset: **MNIST** (digit classification).
- Achieved ~99.2% validation accuracy.
- Stored trained model artifacts in an S3 bucket.

### ✅ Step 2: Model Deployment
- Deployed the trained model to a **C5.large** instance using:
  - **Elastic Inference Accelerator**: `eia1.medium`.
- Created an endpoint named `keras-tf-mnist-*`.

### ✅ Step 3: Inference
- Selected 5 random test images.
- Made predictions using the deployed endpoint.
- Predictions were accurate, e.g., model correctly identified digits like `6, 7, 8, 1, 6`.

### ✅ Step 4: Hyperparameter Tuning with SageMaker
- Tuned:
  - `epochs`: [5, 20]
  - `learning_rate`: [0.0001, 0.1] (log scale)
  - `batch_size`: [32, 1024]
- Objective metric: `val_acc` (validation accuracy).
- Used:
  - `max_jobs=10`, `max_parallel_jobs=2`.
- Final tuned values:
  - `epochs`: 19
  - `learning_rate`: 0.00087
  - `batch_size`: 576
  - Accuracy: ~99.22%
- Best model was automatically deployed using `tuner.deploy()`.
![image](https://github.com/user-attachments/assets/2a25eb01-60dc-40c4-b75d-df703af41572)
![image](https://github.com/user-attachments/assets/79ba04ad-8ddf-466b-9753-168f6fef23a7)

## 🧹 Cleanup
- Deleted endpoint using: `sess.delete_endpoint(endpoint_name)`
- Stopped notebook instance to avoid additional charges.


