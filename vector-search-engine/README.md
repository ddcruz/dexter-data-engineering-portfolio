# Vector Search Engine on Databricks

## 📌 Project Overview
A vector search engine using embeddings and Databricks Vector Index (or FAISS).

## 🏗️ Architecture Diagram

        +----------------------+
        |  Raw Text / Docs     |
        +----------+-----------+
                   |
                   v
        +----------------------+
        | Embedding Generator  |
        | (HF / OpenAI)        |
        +----------+-----------+
                   |
                   v
        +----------------------+
        | Vector Index         |
        | (FAISS / Databricks) |
        +----------+-----------+
                   |
                   v
        +----------------------+
        | Similarity Search API|
        +----------------------+


## 🛠️ Tech Stack
- Databricks
- HuggingFace / OpenAI embeddings
- Vector Index / FAISS
- Python API

## ✨ Features
- Embedding generation
- Vector index creation
- Similarity search API
- Notebook demo

## 📂 Project Structure
notebooks/
api/
embeddings/


## 🚀 How to Run
1. Generate embeddings  
2. Build vector index  
3. Run API for similarity search  

## 🧠 Design Decisions
- Why vector search  
- Embedding model selection  

## 🔮 Future Enhancements
- Add RAG pipeline  
- Add semantic caching  

## 📚 Key Learnings
(Add your reflections)
