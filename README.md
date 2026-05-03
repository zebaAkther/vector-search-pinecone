# 🔎 Vector Search with Pinecone

### *Scalable Semantic Search Engine using Sentence Transformers & Pinecone*

---

## 🧠 Abstract

This project implements a **scalable semantic search engine** using **vector embeddings and Pinecone**, a cloud-native vector database. It enables intelligent information retrieval by understanding the **semantic meaning of queries**, rather than relying on keyword matching.

The system demonstrates a transition from **local vector search (FAISS)** to **production-grade cloud search**, making it suitable for real-world applications like:

* Enterprise knowledge bases
* AI chatbots
* Retrieval-Augmented Generation (RAG) systems

---

## 🚀 Overview

This application allows users to:

* Upload text-based datasets
* Convert them into vector embeddings
* Store and index them in **Pinecone**
* Perform real-time semantic search using natural language queries

---

## 🎯 Key Features

* 📄 Upload custom text dataset
* 🧠 Semantic search using Sentence Transformers
* ☁️ Cloud-based vector storage with Pinecone
* ⚡ Fast and scalable similarity search
* 🎛️ Adjustable top-K results
* 💬 Natural language querying
* 🎨 Clean Streamlit UI

---

## 🏗️ System Architecture

```text id="arch_pc"
User Query → Embedding Model → Pinecone Index → Similarity Search → Ranked Results
```

---

## ⚙️ Tech Stack

* **Language:** Python
* **Frontend:** Streamlit
* **Embedding Model:** Sentence Transformers (`all-MiniLM-L6-v2`)
* **Vector Database:** Pinecone
* **Libraries:** NumPy

---

## 📂 Project Structure

```bash id="proj_pc"
vector-search-pinecone/
│
├── app.py                  # Streamlit app
├── Employee.txt            # Sample dataset
├── requirements.txt
└── README.md
```

---

## 🧠 How It Works

### 1. Document Ingestion

* Upload `.txt` file
* Text is split into individual documents

---

### 2. Embedding Generation

```python id="pc_emb"
model.encode(documents)
```

* Converts text into dense vector representations
* Captures semantic meaning

---

### 3. Pinecone Indexing

```python id="pc_idx"
index.upsert(vectors)
```

* Stores embeddings in cloud
* Enables scalable search

---

### 4. Query Processing

```python id="pc_query"
index.query(vector=query_embedding, top_k=k)
```

* Finds most similar vectors
* Returns ranked results

---

## 📊 Example Dataset

Sample Q&A:

* Q: *Are we allowed to work from home?*
  A: Yes, up to 2 days per week

* Q: *What is the notice period?*
  A: 30 days

* Q: *How do I contact HR?*
  A: Email [hr@company.com](mailto:hr@company.com)

---

## ▶️ Run the Application

### 1. Clone repository

```bash id="runpc1"
git clone https://github.com/zebaAkther/vector-search-pinecone.git
cd vector-search-pinecone
```

---

### 2. Install dependencies

```bash id="runpc2"
pip install -r requirements.txt
```

---

### 3. Set Pinecone API Key

```bash id="runpc3"
export PINECONE_API_KEY="your_api_key"
```

---

### 4. Run app

```bash id="runpc4"
streamlit run app.py
```

---

### 5. Open browser

```text id="runpc5"
http://localhost:8501
```

---

## 📸 Demo

### 🔹 Pinecone Semantic Search UI

<img width="1432" height="859" alt="Screenshot 2026-04-25 at 9 40 43 PM" src="https://github.com/user-attachments/assets/d29eb9b0-f920-427e-8d0f-03d8c273aff1" />

<img width="1440" height="857" alt="Screenshot 2026-04-25 at 9 41 06 PM" src="https://github.com/user-attachments/assets/1affccd3-f078-4e0b-9c16-c83b5eb50f6f" />

---

## 📈 Key Insights

* Semantic search retrieves results based on **meaning, not keywords**
* Pinecone enables **horizontal scalability**
* Vector databases are core to modern AI systems (RAG, LLMs)

---

## ⚖️ FAISS vs Pinecone

| Feature     | FAISS       | Pinecone   |
| ----------- | ----------- | ---------- |
| Storage     | Local       | Cloud      |
| Scalability | Limited     | High       |
| Persistence | Manual      | Built-in   |
| Use Case    | Prototyping | Production |

---

## ⚠️ Important Note

🚨 **Do NOT expose your API key in code**

Instead, use environment variables:

```python id="safe_key"
import os
api_key = os.getenv("PINECONE_API_KEY")
```

---

## 🔮 Future Enhancements

* 🔹 Integrate LLM for answer generation (RAG)
* 🔹 Add PDF/CSV ingestion
* 🔹 Multi-user support
* 🔹 Deploy on cloud (Streamlit Cloud / AWS)
* 🔹 Hybrid search (keyword + vector)

---

## 🧠 Learning Outcomes

* Vector embeddings and semantic similarity
* Cloud-based vector databases
* Scalable AI system design
* Retrieval-based architectures

---

## 👩‍💻 Author

**Zeba Akther**
🔗 GitHub: https://github.com/zebaAkther

---

