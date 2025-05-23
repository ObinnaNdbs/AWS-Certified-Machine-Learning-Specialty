# Amazon S3 Hands-On Labs

This module combines four core S3-focused labs covered during the AWS Certified Machine Learning Specialty course. Each lab explores key operational and configuration concepts of Amazon S3 through hands-on exercises in the AWS Console.

---

## ✅ Covered Labs

### 1. Storage Classes & Tiering
- Created a bucket (`S3-storage-classes-demos-2022`) and uploaded an object.
- Reviewed and modified storage classes (Standard, IA, One Zone-IA, Intelligent-Tiering, Glacier tiers).
- Changed object storage class post-upload.
![image](https://github.com/user-attachments/assets/4922a3f5-4b5d-4a0b-ad83-b49a6b6ca4bd)


### 2. Lifecycle Rules
- Created an S3 lifecycle rule (`DemoRule`) to:
  - Transition objects between storage classes (e.g., Standard-IA → Glacier).
  - Expire current and non-current versions.
  - Permanently delete non-current objects.
  - Visualize the timeline of object transitions.
![image](https://github.com/user-attachments/assets/23424b34-4dc4-4107-bf1e-2e9a7a2a55a7)


### 3. Bucket Policies
- Modified bucket permission settings to allow public access.
- Used AWS Policy Generator to:
  - Create a public `GetObject` bucket policy.
  - Apply policy and verify public URL access for an image.
![image](https://github.com/user-attachments/assets/9b50373c-00d1-4dd9-a0a6-cf6d355172b1)

### 4. Server-Side Encryption
- Created an encrypted bucket (`demo-encryption-stephane-v2`) with versioning.
- Uploaded files with:
  - Default SSE-S3 encryption.
  - Overridden SSE-KMS encryption using AWS/S3 default KMS key.
- Reviewed encryption changes and object versioning behavior.
- Explored console limits (e.g., SSE-C and client-side encryption require CLI).
![image](https://github.com/user-attachments/assets/4fa5676e-66d6-44c5-ac58-18dd9346b3e2)

---
