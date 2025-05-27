# Lab: Custom TensorFlow Model Training in SageMaker

This lab demonstrates how to take a custom Convolutional Neural Network (CNN) built with TensorFlow/Keras and run it within the Amazon SageMaker framework for training. We adapt a pre-existing MNIST handwriting recognition model and deploy it in two ways: locally on a notebook instance and remotely on a GPU-backed training job.

## Objectives

- Upload and organize the MNIST dataset
- Adapt a TensorFlow/Keras CNN for use with SageMaker
- Train and test the model locally on a notebook instance
- Train the model at scale using a P3 GPU instance on SageMaker

## Steps Performed

1. **Setup**
   - Launch a Jupyter Notebook instance in SageMaker
   - Upload two files:
     - `mnist-train-cnn.py` (TensorFlow CNN model with argument parsing)
     - `keras-mnist-sagemaker.ipynb` (Notebook to run training)

2. **Data Preparation**
   - Use built-in Keras functions to load the MNIST dataset
   - Store training and validation data locally in `/data/train` and `/data/validation`
   - Upload the `.npz` files to an S3 bucket (`sagemaker-keras-mnist`)

3. **Local Training**
   - Run the custom CNN locally on the notebook instance using:
     ```python
     !python mnist-train-cnn.py
     ```
   - Validate that the script runs correctly for one epoch
   - Achieved ~98.4% validation accuracy

4. **GPU-based Remote Training**
   - Configure a `TensorFlow` estimator with:
     - `instance_type='ml.p3.2xlarge'`
     - `epochs=10`
     - `batch_size=32`
     - `learning_rate=0.001`
   - Execute training using:
     ```python
     estimator.fit({'train': train_path, 'validation': val_path})
     ```

## Notes

- Used argument parsing in the training script to allow SageMaker compatibility
- Converted image data and labels into the expected format (one-hot encoded, normalized)
- Added dropout layers to the CNN for regularization
- Training on `ml.p3.2xlarge` is cost-efficient but requires proper AWS account limits

