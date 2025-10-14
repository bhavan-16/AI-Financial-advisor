from openai import OpenAI
import os

class ExpenseTrackerAgent:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def analyze_expenses(self, expenses, income):
        if not expenses:
            return "No expenses mentioned."

        prompt = f"""
        You are an expert personal finance AI.
        The user earns ₹{income} monthly and describes their expenses as: "{expenses}".
        Analyze and suggest where they can cut down or optimize their spending, 
        keeping it practical and encouraging.
        """

        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return completion.choices[0].message.content
