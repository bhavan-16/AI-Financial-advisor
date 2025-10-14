# E:\ai_financial_advisor\rag\retriever.py

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb
import os

# Optional: setup local persistent Chroma DB
PERSIST_DIR = "./rag_storage"

def _get_index():
    if os.path.exists(PERSIST_DIR):
        print("🔁 Loading existing index...")
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        return load_index_from_storage(storage_context)
    else:
        print("⚙️ Creating new index from 'data/' folder...")
        documents = SimpleDirectoryReader("data").load_data()
        index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist(persist_dir=PERSIST_DIR)
        return index

def explain_concept(query: str) -> str:
    """Retrieve explanation for a given financial concept."""
    try:
        index = _get_index()
        retriever = index.as_retriever(similarity_top_k=2)
        response = retriever.retrieve(query)
        if not response:
            return "Sorry, I couldn't find an explanation for that concept."
        return "\n".join([str(r.node.get_content()) for r in response])
    except Exception as e:
        return f"Error retrieving concept: {e}"
