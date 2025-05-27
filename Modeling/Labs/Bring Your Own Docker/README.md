# 🐳 Bring Your Own Docker (BYO Docker) on Amazon SageMaker

This lab demonstrates how to **build, push, and train a custom Docker container** for machine learning on Amazon SageMaker. Unlike using SageMaker's built-in algorithms or script mode, this workflow gives you **complete control** over the training and hosting environment.
![image](https://github.com/user-attachments/assets/0ec1776b-a71a-4d3a-af43-a420a231d685)

---

## 🛠️ What You Did

1. **Accessed SageMaker Notebook Instances**  
   - Launched a Jupyter notebook from an existing SageMaker instance.

2. **Selected BYO Docker Example**
   - Opened the `tune_or_bring_your_own.ipynb` example notebook.
   - Made a local copy to work from.

3. **Retrieved the SageMaker Execution Role**
   - Used for AWS permission handling within the notebook.

4. **Used 3 Essential Files**
   - `Dockerfile`: Defines the container build steps.
   - `ms.R`: Custom training script (in R).
   - `plumber.R`: Script for serving the model during inference.

5. **Built and Pushed Docker Image**
   - Constructed your own Docker image.
   - Pushed the image to **Amazon Elastic Container Registry (ECR)**.

6. **Prepared Data**
   - Split your dataset into training and testing sets.

7. **Initialized a Custom Estimator**
   - Provided the **ECR image URI** to the estimator.
   - Ran `estimator.fit()` to train the model using your container.

---

## 🔧 Tools Used

- **Amazon SageMaker**
- **Amazon ECR**
- **Jupyter Notebooks**
- **Docker (Custom image)**
- **R Scripts** (`ms.R`, `plumber.R`)

---

This lab is ideal for demonstrating end-to-end containerization and custom model training on SageMaker — showcasing full environment control, a key skill in production ML systems.
