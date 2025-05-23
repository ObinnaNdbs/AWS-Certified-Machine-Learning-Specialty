# 🧱 1_Basics_AWS

This directory contains foundational AWS configurations and hands-on labs that prepare the environment for scalable, secure, and cost-efficient machine learning workflows. These skills are essential for working in cloud-based ML pipelines and infrastructure.

---

## ✅ Included Labs & Concepts

| Lab | Description |
|-----|-------------|
| `setup_sagemaker_notebook.md` | Provisioned and configured a SageMaker notebook instance for development and experimentation. |
| `iam_basics.md` | Created and tested IAM roles, policies, and permission boundaries for secure resource access. |
| `s3_bucket_setup.md` | Deployed S3 buckets with versioning, encryption (AES-256), and lifecycle policies for cost optimization. |
| `vpc_and_billing_alerts.md` | Created VPC endpoints to route traffic privately and implemented AWS billing alarms via CloudWatch. |
| `default_encryption.md` | Enforced default encryption settings for new S3 objects across all data buckets. |

---

## 🛠️ Skills Demonstrated

- 🔐 IAM Roles and Policies  
- 🗃️ Amazon S3: Bucket Policy, Encryption, Versioning, Lifecycle Rules  
- 📓 SageMaker Notebook Provisioning  
- 🌐 VPC Endpoints for Secure Access  
- 💸 Billing Alerts and Cost Monitoring with CloudWatch

---

## 📸 Screenshots to Include (place in `/assets/` folder)

| Image File | Description |
|------------|-------------|
| `sagemaker_instance.png` | Screenshot of SageMaker notebook instance configuration (instance type, IAM role, status) |
| `iam_policy_custom.png` | Screenshot of a custom IAM policy or trust relationship setup |
| `s3_bucket_settings.png` | S3 bucket encryption and lifecycle rule UI |
| `billing_alert.png` | Billing alarm rule or budget threshold from AWS Budgets or CloudWatch |
| `vpc_endpoint.png` | VPC endpoint configuration screen (S3 or SageMaker) |

---

## 📘 Context

All configurations were completed using the AWS Free Tier (where applicable) and follow best practices in cloud security, access control, and cost management. This section serves as the backbone for all subsequent ML workflows in the pipeline.

