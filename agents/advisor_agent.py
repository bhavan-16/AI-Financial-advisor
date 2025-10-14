from agents.expense_tracker_agent import ExpenseTrackerAgent
from agents.investment_planner_agent import InvestmentPlannerAgent
from openai import OpenAI
import os

class AdvisorAgent:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.expense_agent = ExpenseTrackerAgent()
        self.investment_agent = InvestmentPlannerAgent()

    def get_advice(self, income, expenses, goals):
        expense_tip = self.expense_agent.analyze_expenses(expenses, income)
        investment_tip = self.investment_agent.plan_investments(income, goals)

        # Combine all into a coherent GPT-generated summary
        system_prompt = """
        You are a financial advisor AI. 
        Combine multiple agent suggestions (expense + investment) into a clear, actionable financial summary.
        Write in a friendly and simple tone.
        """

        user_prompt = f"""
        Income: ₹{income}
        Expense feedback: {expense_tip}
        Investment advice: {investment_tip}
        Goals: {goals}
        """

        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )

        return completion.choices[0].message.content
