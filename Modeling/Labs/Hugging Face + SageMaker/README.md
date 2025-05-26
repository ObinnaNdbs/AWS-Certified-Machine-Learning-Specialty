# 🤗 Hugging Face Deployment with Amazon SageMaker

This lab demonstrates **three** practical approaches to deploying Hugging Face Transformer models using Amazon SageMaker:

---

## 🧪 Lab Objectives

- Deploy a Hugging Face model **trained within SageMaker**
- Deploy a **pre-trained model saved in Amazon S3**
- Deploy a **ready-made Hugging Face model directly from HuggingFace Hub**

---

## ✅ Method 1: Deploying a Trained Model on SageMaker

1. Instantiate a `HuggingFace` estimator using `sagemaker.huggingface`.
2. Fit the model on training data.
3. Deploy the trained model with:
   ```python
   estimator.deploy(instance_type="ml.m5.xlarge", instance_count=1)
4. Predict using the returned predictor.

## ✅ Method 2: Deploying a Model from S3

1. Specify SageMaker role.
2. Use `HuggingFaceModel` class:

```bash
from sagemaker.huggingface import HuggingFaceModel

huggingface_model = HuggingFaceModel(
  model_data='s3://path/to/model.tar.gz',
  role=role,
  transformers_version='x',
  pytorch_version='x'
)
```
3. Deploy the model:

```bash
predictor = huggingface_model.deploy(
  initial_instance_count=1,
  instance_type="ml.m5.xlarge"
)
```
4. Run predictions using predictor.predict(data).
5. Clean up by deleting the endpoint and model.

## ✅ Method 3: Deploying a Ready-Made Model from Hugging Face Hub

1. Define model metadata:
```bash
hub = {
  'HF_MODEL_ID': 'distilbert-base-uncased',
  'HF_TASK': 'question-answering'
}
```

2. Instantiate the Hugging Face model:
```bash
huggingface_model = HuggingFaceModel(
  env=hub,
  role=role,
  transformers_version='x',
  pytorch_version='x'
)
```
3. Deploy and perform inference:
```bash
predictor = huggingface_model.deploy(
  initial_instance_count=1,
  instance_type="ml.m5.xlarge"
)

predictor.predict({"inputs": "What is AWS?"})
```
4. Clean up resources.

## 🧼 Cleanup
Always remember to:
```bash
predictor.delete_endpoint()
huggingface_model.delete_model()
```

