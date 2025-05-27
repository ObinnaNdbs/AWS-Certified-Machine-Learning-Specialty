# Lab 1: Setting Up a Custom TensorFlow CNN in SageMaker

## Overview

This lab demonstrates how to deploy and prepare a custom **Convolutional Neural Network (CNN)** model built with **TensorFlow/Keras** in the Amazon SageMaker environment. We set up a SageMaker notebook instance, configure permissions, and upload necessary files to prepare for model training and inference.

## Objectives

- Launch a SageMaker notebook instance (`t2.medium`)
- Configure IAM roles and access permissions to S3
![image](https://github.com/user-attachments/assets/e56538a0-c18a-4c1e-a828-2d84061ac23a)
- Upload a custom CNN training script and Jupyter notebook
- Prepare the environment for model training and deployment in SageMaker
![image](https://github.com/user-attachments/assets/077f3f0f-85f8-443e-90cc-b330619d7114)

## Tools & Services Used

- **Amazon SageMaker**: Notebook Instances, Console
- **AWS IAM**: Role creation and permissions for accessing S3
- **Amazon S3**: For hosting the input data
- **TensorFlow/Keras**: For CNN model code and training
- **Jupyter Notebook**: `keras-mnist-sagemaker.ipynb`

## Files Uploaded

- `mnist-train-cnn.py`: TensorFlow CNN training script
- `keras-mnist-sagemaker.ipynb`: Notebook walkthrough for training and deployment

## Key Concepts Illustrated

- Creating a SageMaker notebook instance
- Understanding Elastic Inference (though not yet used)
- IAM role creation and basic S3 access management
- Uploading and opening notebooks in SageMaker

---


