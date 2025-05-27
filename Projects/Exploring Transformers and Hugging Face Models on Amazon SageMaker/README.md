# Project: Exploring Transformers and Hugging Face Models on Amazon SageMaker

This project walks through hands-on experimentation with transformer-based models using Amazon SageMaker and Hugging Face. We explore tokenization, positional encoding, self-attention visualization, and text generation using pre-trained models like BERT and GPT-2.

---

## ✅ Objectives

- Launch a SageMaker notebook instance for transformer experimentation
- Install and use the Hugging Face `transformers` package
- Tokenize and visualize input sentences
- Understand and plot positional encoding
- Visualize self-attention with BERT
- Generate text using GPT-2 via Hugging Face pipelines

---

## 🛠 Tools & Technologies

- **Amazon SageMaker**
- **Hugging Face Transformers**
- **BERT** (for tokenization and attention)
- **GPT-2** (for text generation)
- **PyTorch**
- **Jupyter Notebook**
- **Matplotlib**
- **BertViz**
- **Transformers Pipelines**

---

## 🧪 Activities

### 1. **SageMaker Notebook Setup**
- Created a T3.medium SageMaker notebook instance
- Uploaded and ran `Transformers_MLCourse_SageMaker.ipynb`
- Installed required packages:  
  `transformers`, `ipywidgets`, `bertviz`, `xformers`, `evaluate`, `matplotlib`, `torch`
![image](https://github.com/user-attachments/assets/81196bb2-d72d-4311-a282-19057411b4fd)

### 2. **Tokenization and Positional Encoding**
- Tokenized the sentence *"I read a good novel."*
- Explored special tokens (`[CLS]`, `[SEP]`, punctuation)
- Visualized positional encoding using sin/cos wave matrices via `matplotlib`
![image](https://github.com/user-attachments/assets/bce7df13-2b42-4bc0-8dc2-5575e2987492)
![image](https://github.com/user-attachments/assets/5dfddad1-8e65-4a9a-85bf-e54d68f7d6fc)

### 3. **Visualizing Self-Attention**
- Used `bertviz` to display self-attention heads
- Compared how the transformer interprets the word "novel" in two different sentences:
  - *"I read a good novel."*
  - *"Attention is a novel idea."*
- Highlighted context-sensitive word interpretation via self-attention layers
![image](https://github.com/user-attachments/assets/04d4367b-86a0-40c7-aa01-0ae191ad6a5a)
![image](https://github.com/user-attachments/assets/c7b152b6-6df5-42da-bf36-c5abd3170a4e)

### 4. **Text Generation with GPT-2**
- Used Hugging Face `pipeline()` to load and generate text with GPT-2
- Generated responses to prompts:
  - *"I read a good novel..."*
  - *"This movie seemed really long..."*
  - *"Star Trek..."*
- Adjusted:
  - `max_length`
  - `num_return_sequences`
![image](https://github.com/user-attachments/assets/1104996a-c0f4-4d02-88de-b2f57f818213)

---

## 📎 Files Used
- `Transformers_MLCourse_SageMaker.ipynb` – Notebook for the full project
- Pretrained models from Hugging Face:
  - `bert-base-uncased`
  - `gpt2`

---

## 💰 Billing Reminder
This project runs on a paid SageMaker instance. To avoid unnecessary charges, always **STOP** the notebook instance after use.

---

## 📚 Summary
This project demystifies key elements of transformer models and shows how easily Hugging Face's ecosystem integrates with SageMaker for hands-on experimentation. Through tokenization, attention visualization, and generation tasks, users gain an intuitive understanding of how modern LLMs operate under the hood.

