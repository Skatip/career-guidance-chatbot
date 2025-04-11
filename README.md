An intelligent, real-time RAG (Retrieval-Augmented Generation) chatbot that helps students explore career options, learn required skills, and discover top courses — all powered by open-source LLMs and local embeddings.

✨ Features
✅ Natural language Q&A about career paths
✅ Local knowledge base using ChromaDB
✅ LLM-powered explanations (Mistral or Hugging Face API)
✅ Streamlit chatbot UI
✅ FastAPI backend with REST endpoints
✅ Docker-ready, deployable on Hugging Face/Render
✅ Evaluation metrics (similarity, ROUGE-L)
✅ GitHub Actions CI for linting

🧠 How It Works
User asks a career-related question
Query is embedded and matched with relevant documents using ChromaDB
Retrieved context is passed to an LLM (local or remote)
Final answer is generated and displayed with evaluation metrics
🛠 Tech Stack
FastAPI – API backend
Streamlit – Frontend chatbot
sentence-transformers – Embedding model
ChromaDB – Vector store for retrieval
transformers – Local LLM (Mistral 7B Instruct)
Hugging Face Inference API – Optional fallback
Docker – For containerized deployment
