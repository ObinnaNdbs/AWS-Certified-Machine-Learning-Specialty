# Lab: Creating a Labeling Job using Amazon SageMaker Ground Truth

## Overview
This lab involved setting up a **bounding box labeling job** for a dataset of bee images using **Amazon SageMaker Ground Truth**. We performed the full labeling workflow from dataset preparation to live annotation using a private workforce.
![image](https://github.com/user-attachments/assets/84477400-64ac-4810-b410-0e9646d14b6e)

## Steps Covered
- Accessed **Amazon SageMaker > Ground Truth > Labeling Jobs**
- Chose **Automated Data Setup**
- Specified:
  - **Input S3 location**: Path to bee images
  - **Output S3 location**: Same as input
  - **Data type**: Image
- Created a new **IAM role** with read/write permissions for the bucket
- Selected **Full dataset** labeling (not random sample)
- Chose **Bounding Box** as the task type
- Configured workforce:
  - Selected **Private Workforce**
  - Assigned email-based workforce team
  - Defined job description and labeling class ("bee")
- Launched the labeling job
- Demonstrated annotation:
  - Annotator drew bounding boxes around bees
  - Submitted results per image
![image](https://github.com/user-attachments/assets/19182f70-9d58-47ec-a21d-7d40f5a4a68e)

## Outcome
A running labeling job where each of the 33 bee images were queued for annotation with bounding boxes through the private workforce.
