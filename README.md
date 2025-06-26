
# 🧠 VaultRAG

> **Private. Offline. Open-Source. Secure.**  
> Local Retrieval-Augmented Generation (RAG) system using open-source LLMs—without sending your data to the cloud.

![Demo](demo.gif)

---

## ✨ Features

- 🔒 **Fully Offline**: No API keys, no external calls—your data stays private.
- 📄 **Multi-format File Support**: Ingest PDFs, DOCX, and text files effortlessly.
- 🧩 **Modular Architecture**: Customize loaders, chunkers, vector stores, and LLMs.
- 🧠 **LLM Flexibility**: Works with Ollama, LLaMA, Mistral, and other local models.
- ⚡ **Fast Retrieval**: Uses vector embeddings and similarity search for quick responses.
- 🌐 **Streamlit UI**: Simple, intuitive frontend for interacting with your local knowledge base.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/honey1205/VaultRAG.git
cd VaultRAG
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

> ⚠️ Make sure you're using a Python 3.10+ environment.

### 3. Run the App

```bash
streamlit run app.py
```

---

## 📁 Folder Structure

```bash
VaultRAG/
├── app.py               # Streamlit app
├── ingest.py            # File loader and vector store builder
├── query.py             # Handles RAG logic
├── utils/               # Utility functions
├── data/                # Your source files go here
├── vectorstore/         # Persisted embeddings
└── requirements.txt     # Python dependencies
```

---

## 🔧 Configuration

You can modify model behavior, chunk size, or retriever type in `config.py`. Default setup uses `llama_index` with `Ollama`.

---

## 📌 Example Models

Use with local models like:

- `llama2`
- `mistral`
- `gemma`
- `codellama`

```bash
ollama run mistral
```
