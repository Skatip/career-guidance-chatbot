
# 🎓 AI Career Guidance Chatbot using RAG

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-orange)
![FastAPI](https://img.shields.io/badge/API-FastAPI-green)
![License](https://img.shields.io/badge/license-MIT-brightgreen)
![GitHub Actions](https://github.com/your-username/career-guidance-chatbot/actions/workflows/ci.yml/badge.svg)

An intelligent, real-time **RAG (Retrieval-Augmented Generation)** chatbot that helps students explore career options, learn required skills, and discover top courses — all powered by open-source LLMs and local embeddings.

---

## ✨ Features

✅ Natural language Q&A about career paths  
✅ Local knowledge base using ChromaDB  
✅ LLM-powered explanations (Mistral or Hugging Face API)  
✅ Streamlit chatbot UI  
✅ FastAPI backend with REST endpoints  
✅ Docker-ready, deployable on Hugging Face/Render  
✅ Evaluation metrics (similarity, ROUGE-L)  
✅ GitHub Actions CI for linting

---

## 🧠 How It Works

1. User asks a career-related question  
2. Query is embedded and matched with relevant documents using **ChromaDB**  
3. Retrieved context is passed to an **LLM** (local or remote)  
4. Final answer is generated and displayed with evaluation metrics  

---

## 🛠 Tech Stack

- `FastAPI` – API backend  
- `Streamlit` – Frontend chatbot  
- `sentence-transformers` – Embedding model  
- `ChromaDB` – Vector store for retrieval  
- `transformers` – Local LLM (Mistral 7B Instruct)  
- `Hugging Face Inference API` – Optional fallback  
- `Docker` – For containerized deployment  

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/your-username/career-guidance-chatbot.git
cd career-guidance-chatbot
```

### 2. Install dependencies
```bash
pip install -r deployment/requirements.txt
```

### 3. Setup `.env`
```env
HUGGINGFACE_API_TOKEN=your_huggingface_token_here
```

### 4. Embed your dataset
```bash
python backend/embed_data.py
```

### 5. Run the app
```bash
uvicorn backend.main:app --reload
streamlit run frontend/app.py
```

---

## 🐳 Run with Docker

```bash
docker build -t career-chatbot .
docker run -p 8000:8000 career-chatbot
```

---

## 🧪 Evaluation

The chatbot calculates:
- **Cosine Similarity** between query and retrieved content
- **ROUGE-L Score** to measure LLM output quality
- Logging of every query-response pair with timestamps

---

## 📁 Project Structure

```
career-guidance-chatbot/
│
├── backend/        # FastAPI, RAG, logger, metrics
├── frontend/       # Streamlit chatbot
├── models/         # Embedding & LLM config
├── data/           # Sample career data
├── deployment/     # Dockerfile, requirements.txt
├── notebooks/      # EDA and prototype work
├── .github/        # CI workflows
├── .env            # Secrets file
└── main.py         # Entry point
```

---

## 📸 Screenshots

> _(Add screenshots of chatbot UI, evaluation results, etc.)_

---

## 📜 License

This project is licensed under the MIT License.

---

## 🤝 Contributions

PRs are welcome! Please open an issue first to discuss proposed changes.

---

## 📬 Contact

Built with ❤️ by [Your Name](https://github.com/your-username)
