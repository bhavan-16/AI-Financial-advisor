Production-Grade RAG System using Inngest, FastAPI, Qdrant & Streamlit

This project implements a Retrieval-Augmented Generation (RAG) pipeline that allows users to upload PDFs, index their content, and ask intelligent, context-aware questions about them.
It combines AI, vector databases, and event-driven architecture to ensure scalability, performance, and reliability.


Features:

PDF Upload & Ingestion: Upload PDF documents via Streamlit interface.

Automated Workflow Orchestration: Inngest triggers background workflows for ingestion and querying.

Vector Storage: Qdrant stores embeddings for semantic search.

AI-Powered Q&A: Uses OpenAI’s GPT model to generate answers based on document context.

Asynchronous Processing: FastAPI and Inngest enable non-blocking background jobs.

Secure API Keys Management: dotenv used for environment variable handling.
