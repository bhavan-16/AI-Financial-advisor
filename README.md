AI Financial Advisor

Overview:
AI Financial Advisor is an intelligent financial planning system designed to help users manage income, expenses, and savings goals effectively. It provides personalized financial recommendations using AI-driven analysis and retrieval-augmented generation (RAG). The system explains financial concepts in simple language, helping users make informed financial decisions.

Features:
Personalized Advice: Generates tailored financial plans based on income, spending habits, and goals.
Expense Tracking: Analyzes expense patterns and provides saving suggestions.
Goal Planning: Recommends strategies for achieving financial targets.
Concept Explanation: Retrieves and explains financial terms using RAG.
User-Friendly Interface: Built with Streamlit for smooth interaction.

Tech Stack:
Frontend: Streamlit
Backend: Python
AI Frameworks:
OpenAI API (for language understanding and reasoning)
LlamaIndex (for document indexing and querying)
ChromaDB (as the vector database for retrieval)
Environment Management: dotenv
Dependency Management: pip / requirements.txt

Project Architecture:
The system follows a multi-agent architecture:
Expense Tracker Agent – Analyzes user spending habits.
Goal Planner Agent – Suggests savings and investment strategies.
Knowledge Agent (RAG) – Retrieves and explains financial terms.
Advisor Agent – Combines insights from all agents and provides final recommendations.

Project Flow:
User inputs income, expenses, and goals via Streamlit UI.
Advisor Agent coordinates with Expense and Goal Agents to generate insights.
RAG system retrieves relevant financial data using LlamaIndex and ChromaDB.
OpenAI model generates a final personalized recommendation.
Output is displayed to the user in an explainable and interactive format.
