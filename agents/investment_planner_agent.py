from openai import OpenAI
import os

class InvestmentPlannerAgent:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def plan_investments(self, income, goals):
        if not goals:
            return "No financial goals mentioned."

        prompt = f"""
        You are a financial investment advisor AI.
        The user earns ₹{income} monthly and has the goal: "{goals}".
        Suggest an investment plan using Indian financial options 
        (like SIPs, mutual funds, PPF, RDs, etc.).
        Include specific percentage splits and reasoning in simple language.
        """

        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return completion.choices[0].message.content
