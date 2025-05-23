# 🛠️ Hands-On Notes – AWS Basics

This document outlines the key foundational AWS services and concepts I practiced hands-on. Each section is followed by space for visuals (screenshots, CLI outputs) to demonstrate actual execution or configuration.

---

## 🔐 1. IAM – Identity and Access Management

### What I Did:
- Created IAM users and groups
- Assigned permission policies (e.g., `AmazonS3FullAccess`)
- Generated access keys for CLI access
- Created roles and explored trust relationships

> _Why it's important:_ IAM is essential for defining who can do what in AWS. It underpins all security best practices in the cloud.

![image](https://github.com/user-attachments/assets/3b3a58d3-f578-4e05-b20a-af6cfaee156c)


---

## 💾 2. AWS Storage Services – S3, EBS, EFS, FSx

### What I Did:
- Created an S3 bucket with versioning and encryption enabled
- Uploaded and accessed objects using the AWS Console and CLI
- Created and attached an EBS volume to an EC2 instance
- Briefly explored EFS and FSx setup screens

> _Why it's important:_ These storage services support different workloads — S3 for object storage, EBS for block storage, EFS for scalable NFS file systems, and FSx for Windows-based file systems.

![image](https://github.com/user-attachments/assets/f19d9654-a9ab-47c9-9103-1355b2a5157f)


---

## 💻 3. EC2 – Elastic Compute Cloud

### What I Did:
- Launched an EC2 instance using Amazon Linux 2
- Configured security groups to allow SSH
- Connected via terminal and performed basic package installation
- Created a custom Amazon Machine Image (AMI) from an instance

> _Why it's important:_ EC2 is the backbone of compute in AWS. Understanding instance launch, configuration, and SSH access is foundational.

![image](https://github.com/user-attachments/assets/3189a8a0-17af-46ac-bd53-911000615c64)

---

## 📊 4. AWS CloudWatch – Monitoring & Alarms

### What I Did:
- Set up a CloudWatch alarm to monitor EC2 CPU utilization
- Created a billing alarm with SNS notification
- Visualized metric graphs

> _Why it's important:_ CloudWatch provides operational visibility. Setting alarms ensures proactive responses to performance or budget issues.

![image](https://github.com/user-attachments/assets/55535647-5586-4be3-9621-a4fae8a0d963)

---

## 🌎 5. AWS Regions & Availability Zones

### What I Did:
- Explored region selection dropdown
- Launched EC2 instances in different regions
- Compared pricing differences and latency

> _Why it's important:_ AWS is global, but resources are regional. Understanding regions helps with availability, compliance, and cost management.

![image](https://github.com/user-attachments/assets/d74d2af9-be23-4115-adc7-6c7825147bd2)

---

## 💰 6. Billing & Budgets

### What I Did:
- Set up a billing dashboard and budget alarms
- Activated cost explorer
- Used price calculator to simulate multi-service pricing

> _Why it's important:_ Without careful tracking, cloud costs can spiral. Setting alerts and using cost estimators helps stay in control.

![image](https://github.com/user-attachments/assets/2152f198-d580-4705-afa8-8082c6e0e858)

---

## ✅ Summary

These hands-on exercises gave me foundational AWS experience, critical for more advanced ML topics like SageMaker, Glue, or MLOps pipelines. This section ensured I could confidently:
- Navigate the console and CLI
- Launch resources with correct permissions
- Monitor and manage basic AWS services
