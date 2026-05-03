import streamlit as st
import numpy as np
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone, ServerlessSpec
import uuid

# -------------------- CONFIG --------------------
st.set_page_config(page_title="Pinecone Search", page_icon="🔎", layout="wide")

# -------------------- STYLING --------------------
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.main {
    background: linear-gradient(135deg, #0e1117, #1c1f26);
}
.title {
    font-size: 40px;
    font-weight: bold;
    text-align: center;
    color: #00d4ff;
}
.subtitle {
    text-align: center;
    color: gray;
    margin-bottom: 30px;
}
.box {
    background: #1f2937;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
}
.result-box {
    background: #111827;
    padding: 15px;
    border-radius: 12px;
    margin-top: 10px;
    border-left: 4px solid #00d4ff;
}
</style>
""", unsafe_allow_html=True)

# -------------------- TITLE --------------------
st.markdown('<div class="title">🔎 Pinecone Semantic Search</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">FAISS ➝ Pinecone Upgrade 🚀</div>', unsafe_allow_html=True)

# -------------------- LOAD MODEL --------------------
model = SentenceTransformer("all-MiniLM-L6-v2")

# -------------------- PINECONE SETUP --------------------
PINECONE_API_KEY = "pcsk_2DK2kz_RTm8tQ1638yreLUVXdDJcno97oLUvhVBvbdQJ9f28KSPS6KfA5fvx2c4AbommbE"
INDEX_NAME = "rag-project"

pc = Pinecone(api_key=PINECONE_API_KEY)

# Create index if not exists
if INDEX_NAME not in pc.list_indexes().names():
    pc.create_index(
        name=INDEX_NAME,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

index = pc.Index(INDEX_NAME)

# -------------------- SIDEBAR --------------------
st.sidebar.header("⚙️ Settings")
top_k = st.sidebar.slider("Number of Results", 1, 10, 5)

# -------------------- FILE UPLOAD --------------------
st.markdown('<div class="box">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("📂 Upload your text file", type=["txt"])

documents = []

if uploaded_file:
    text = uploaded_file.read().decode("utf-8")
    documents = text.split("\n")

    st.success(f"✅ {len(documents)} documents loaded")

    if st.button("🚀 Upload to Pinecone"):
        embeddings = model.encode(documents)

        vectors = []
        for i, emb in enumerate(embeddings):
            vectors.append({
                "id": str(uuid.uuid4()),
                "values": emb.tolist(),
                "metadata": {"text": documents[i]}
            })

        index.upsert(vectors)
        st.success("🔥 Data uploaded to Pinecone!")

st.markdown('</div>', unsafe_allow_html=True)

# -------------------- SEARCH --------------------
query = st.text_input("💬 Ask your question")

if query:
    query_embedding = model.encode([query])[0]

    results = index.query(
        vector=query_embedding.tolist(),
        top_k=top_k,
        include_metadata=True
    )

    st.markdown("## 🔍 Results")

    for match in results["matches"]:
        st.markdown(f"""
        <div class="result-box">
            <b>Score:</b> {match['score']:.4f}<br><br>
            {match['metadata']['text']}
        </div>
        """, unsafe_allow_html=True)