# 🧪 Amazon Rekognition + Lambda Object Detection Lab

This hands-on lab demonstrates how to use **Amazon Rekognition's Label Detection API** to identify objects in images stored in an S3 bucket. The process is automated through an **AWS Lambda function**.

---

## 🔧 What We Did

1. **Uploaded Image to S3**
   - Image: `dogcat.jfif`
   - Bucket: `dct-bucket-demo`
![image](https://github.com/user-attachments/assets/c4b7f7e1-4dda-48be-ab20-7654baf97cf5)

2. **Tested Rekognition Label Detection in Console**
   - Verified labels and confidence scores using Rekognition web UI.
![image](https://github.com/user-attachments/assets/2a014afd-c1ee-49f5-b252-045d6de53f84)

3. **Created Lambda Function**
   - Name: `object-detection`
   - Runtime: Python 3.9
   - Purpose: Automate Rekognition analysis on images in S3
![image](https://github.com/user-attachments/assets/e4632835-651f-4466-b852-1cd4467021be)

4. **Set IAM Permissions**
   - Attached two AWS-managed policies to the Lambda role:
     - `AmazonS3ReadOnlyAccess`
     - `AmazonRekognitionReadOnlyAccess`
![image](https://github.com/user-attachments/assets/2b89813e-0fe0-4c4a-81d7-282c470d99ba)

5. **Wrote Python Code in Lambda**
   - Initialized Rekognition client using `boto3`
   - Loaded image from S3
   - Called `detect_labels()` API
   - Printed label predictions with confidence scores
![image](https://github.com/user-attachments/assets/70e6de81-eb04-4191-adb0-9f4e811b4f78)
![image](https://github.com/user-attachments/assets/1a028aa5-fe64-4ca3-aa67-5d064003d4d9)

---

## 🧰 AWS Tools Used

- **Amazon Rekognition**
- **Amazon S3**
- **AWS Lambda**
- **IAM (for permissions)**

---

## 🧠 Key Skills Practiced

- Interfacing AWS Rekognition with Lambda
- Reading S3 objects via Lambda
- Applying `detect_labels()` API
- IAM role management and permissions
- Understanding Rekognition’s label hierarchy (e.g., dog → mammal → animal)

---

## ✅ Summary

This lab showcased an end-to-end workflow for automated image object detection using **Amazon Rekognition + Lambda + S3**. You now know how to trigger Rekognition from Lambda and extract structured label data programmatically.
