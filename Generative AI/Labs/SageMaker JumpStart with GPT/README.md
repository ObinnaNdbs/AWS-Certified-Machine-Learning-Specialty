# 🧠 Lab: Using Amazon SageMaker JumpStart with GPT from HuggingFace

This lab walks through deploying a pre-trained foundation model (LLM) from Hugging Face using Amazon SageMaker JumpStart. You’ll explore model loading, deploying inference endpoints, and executing simple prompts for generation—all via a notebook in SageMaker Studio.

---

## 🛠️ Tools & Services Used

- **Amazon SageMaker JumpStart**
- **SageMaker Studio + Notebook**
- **HuggingFace Falcon-7B-Instruct BF16 model**
- **S3** (for future fine-tuning training data)
- **AWS VPC + Subnet** (required for domain setup)

---

## ✅ Lab Workflow Overview

1. **Navigate to SageMaker JumpStart**
   - Access the Foundation Models tab (new feature).
   - Explore various models including Falcon, Meta, and Amazon variants.

2. **Select & Deploy Falcon-7B-Instruct BF16**
   - Launch pre-built notebook for the model.
   - Automatically installs dependencies and initializes kernel.

3. **SageMaker Domain Setup**
   - Quick setup: define domain name, user profile, and associate with a VPC/subnet.
   - Launch SageMaker Studio for notebook interaction.
![image](https://github.com/user-attachments/assets/26a9b9e1-25e9-489f-a8fd-4649375af44d)

4. **Execute Notebook**
   - Run pre-filled cells to:
     - Load the Falcon model.
     - Create a predictor endpoint.
     - Send text prompts and get model completions.
   - Examples include Q&A, code generation, sentiment classification, and translation.
![image](https://github.com/user-attachments/assets/7d345528-93cd-4abc-8462-662e7788464a)

5. **Prompt Examples Used**
   - *"Tell me about Amazon SageMaker."*
   - *"What is your favorite song?"*
   - Sentiment classification training patterns were illustrated, but not executed.
![image](https://github.com/user-attachments/assets/a0c47eb2-527b-48a0-a5a6-4178a1cefe24)

6. **Deployment Parameters**
   - Specify instance type (e.g., `ml.g5.12xlarge`) during predictor creation.
   - Control temperature, max tokens, top_p, and stop token for output.

7. **💡 Optional: Fine-Tuning Discussion**
   - JSONL format with `prompt`, `completion` pairs.
   - Importance of correct format and optional `.template.json` file.
   - Mention of custom examples like Star Trek chatbot (not executed).
   - Warning: very costly + time-intensive on AWS vs. OpenAI.

8. **⚠️ Shutdown is Critical**
   - Stop predictor endpoint.
   - Shutdown notebook kernel.
   - Delete SageMaker domain and user to avoid ongoing billing.

---

## 📌 Notes

- **We did:**
  - Launch a notebook with a real LLM endpoint.
  - Run inference with prompt responses.
  - Inspect instance types and deployment logic.

---


## 🔚 Summary

Despite some UI bugs and long waits, this lab provides a practical intro to integrating HuggingFace LLMs into AWS workflows using SageMaker JumpStart. This foundational skill is critical for scalable GenAI deployments in production.

