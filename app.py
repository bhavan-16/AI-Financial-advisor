import sys, os
from pathlib import Path
import streamlit as st
from dotenv import load_dotenv

# ============================================================
# 🛠 PATH FIX: Ensure the project root and 'rag' folder are importable
# ============================================================
ROOT_DIR = Path(__file__).resolve().parent
RAG_DIR = ROOT_DIR / "rag"
AGENTS_DIR = ROOT_DIR / "agents"

for path in [ROOT_DIR, RAG_DIR, AGENTS_DIR]:
    if str(path) not in sys.path:
        sys.path.append(str(path))

print(f"✅ Project root added to sys.path: {ROOT_DIR}")
print("📁 Available folders in root:", [p.name for p in ROOT_DIR.iterdir()])

# ============================================================
# 🔧 Imports
# ============================================================
from agents.advisor_agent import AdvisorAgent

# Try importing rag.retriever, fall back to dynamic import if not found
try:
    from rag.retriever import explain_concept
except ModuleNotFoundError:
    import importlib.util
    retriever_path = RAG_DIR / "retriever.py"
    if retriever_path.exists():
        spec = importlib.util.spec_from_file_location("rag.retriever", retriever_path)
        rag_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(rag_module)
        explain_concept = rag_module.explain_concept
        print("✅ Dynamically imported rag.retriever")
    else:
        raise FileNotFoundError("❌ retriever.py not found in rag/ folder")

# ============================================================
# 🌍 Load environment variables (for OpenAI API key, etc.)
# ============================================================
load_dotenv()

# ============================================================
# 🧮 Streamlit App UI
# ============================================================
st.set_page_config(page_title="AI Financial Advisor", page_icon="🧮")

st.title("🧮 AI Financial Advisor Agent")
st.write("Your smart, explainable AI for personal finance planning.")

# User inputs
income = st.number_input("💰 Monthly Income (₹):", min_value=0)
expenses = st.text_area("🧾 Describe your spending habits (e.g., rent, dining, shopping):")
goals = st.text_input("🎯 Your financial goals (e.g., save for car, retirement, etc.):")

# Advisor logic
if st.button("Get Recommendations"):
    with st.spinner("Analyzing your financial data..."):
        advisor = AdvisorAgent()
        response = advisor.get_advice(income, expenses, goals)
        st.success(response)

# Divider
st.markdown("---")

# Concept explanation (RAG part)
st.subheader("📘 Ask: What does this financial term mean?")
query = st.text_input("e.g. What is SIP?")

if st.button("Explain"):
    with st.spinner("Retrieving explanation..."):
        st.info(explain_concept(query))
