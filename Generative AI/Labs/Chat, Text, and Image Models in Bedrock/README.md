# Lab: Chat, Text, and Image Foundation Models in the Bedrock Playground

This lab explores the use of Amazon Bedrock's playground to experiment with different foundation models for text, chat, and image generation. We explored the capabilities of Anthropic Claude models and Stability AI for generating responses and images, configuring inference parameters, and uploading contextual files.

## ✅ Prerequisites

- AWS Console access
- Bedrock model access (approved for Claude and Stability AI models)
- Familiarity with prompt engineering basics

## 🧪 Activities

### 1. **Model Access Requests**
- Requested access to:
  - Claude 2.1 / 3.5 Sonnet (Anthropic)
  - Stability AI SDXL 1.0 (image generation)
- Accepted EULAs for each model
![image](https://github.com/user-attachments/assets/5b9d6dd7-2082-4ba2-87c8-f7ef712a57c6)

### 2. **Chat Playground**
- Used **Claude 3.5 Sonnet** for conversational AI
- Adjusted inference parameters:
  - `Temperature`, `Top P`, `Top K`, `Max Output Tokens`
- Example prompt: *“What is the meaning of life?”*
- Demonstrated contextual memory in multi-turn chats
- Uploaded a `.docx` file (`cfas-bylaws-rev-9.docx`)
  - Asked context-aware questions about uploaded text
  - Example: *“What are the requirements for a quorum in a CFAS board meeting?”*
- Used **System Prompts**
  - Example: *“Always respond in the style of a pirate”*
![image](https://github.com/user-attachments/assets/cb6e27ba-d24b-4983-a082-2677eeb8e236)

### 3. **Text Playground**
- Used **Claude 2.1** for one-shot prompts
- Prompt: *“Write me a poem about AWS in the style of a Shakespearean sonnet”*
- Observed output token usage and latency
![image](https://github.com/user-attachments/assets/fe5fe9ec-0bce-4827-b46f-92a038bc26aa)
![image](https://github.com/user-attachments/assets/48e465fe-66b8-414f-ad81-41e00ee7c18f)

### 4. **Image Playground**
- Used **Stability AI SDXL 1.0**
- Prompt: *“Generate a cartoon style logo of a calico cat wearing headphones”*
- Configured:
  - Negative prompts (optional)
  - Orientation & size
  - Prompt strength & generation steps
  - Random seed (for reproducibility)
![image](https://github.com/user-attachments/assets/a1129ff4-1375-488e-83ad-9fcbbf4e598c)

## 📎 Files Used
- `cfas-bylaws-rev-9.docx` — Uploaded to provide contextual input in chat

---

