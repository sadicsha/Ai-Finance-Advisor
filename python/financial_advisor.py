"""
financial_advisor.py
Uses Hugging Face Inference API with .env for secure API key
"""

from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Get API key from .env — no hardcoded key anymore
HF_API_KEY = os.getenv("HF_API_KEY")
HF_MODEL   = "meta-llama/Meta-Llama-3-8B-Instruct"

client = InferenceClient(
    model = HF_MODEL,
    token = HF_API_KEY
)

SYSTEM_PROMPT = """You are an expert AI Financial Literacy Advisor.
Your role is to:
1. Explain financial concepts in clear, simple, jargon-free language.
2. Generate personalised budgeting plans based on user income, expenses, and goals.
3. Provide scenario-based financial insights (savings growth, debt payoff, investments).
Always structure your response with clear headings, bullet points, and actionable steps.
Keep the tone encouraging, practical, and easy to understand for beginners."""


def _call_llm(prompt: str) -> str:
    try:
        response = client.chat_completion(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user",   "content": prompt},
            ],
            temperature=0.7,
            max_tokens=1500,
        )
        return response.choices[0].message.content
    except Exception as exc:
        return f"⚠️ Hugging Face API error: {str(exc)}"


def explain_concept(concept: str) -> str:
    prompt = (
        f"Explain the financial concept '{concept}' in simple terms for a beginner. "
        "Include: (1) what it means, (2) why it matters, (3) a real-life example, "
        "(4) one actionable tip. Format the answer with clear headings."
    )
    return _call_llm(prompt)


def generate_budget_plan(income: float, expenses: dict, goals: str) -> str:
    expense_lines = "\n".join(
        f"  - {cat}: ₹{amt:,.0f}" for cat, amt in expenses.items()
    )
    total_expenses = sum(expenses.values())
    surplus = income - total_expenses
    prompt = f"""Monthly Income : ₹{income:,.0f}
Monthly Expenses:
{expense_lines}
Total Expenses : ₹{total_expenses:,.0f}
Monthly Surplus: ₹{surplus:,.0f}
Financial Goals: {goals}

Create a detailed personalised budget plan with:
1. Spending breakdown as % of income
2. Areas to cut or optimise
3. Ideal 50/30/20 allocation
4. Step-by-step savings roadmap
5. 3-5 immediate actionable steps"""
    return _call_llm(prompt)


def analyse_scenario(scenario_type: str, params: dict) -> str:
    scenario_map = {
        "savings_growth"     : _savings_growth_prompt,
        "debt_repayment"     : _debt_repayment_prompt,
        "investment_planning": _investment_planning_prompt,
    }
    builder = scenario_map.get(scenario_type)
    if not builder:
        return f"Unknown scenario type: '{scenario_type}'."
    return _call_llm(builder(params))


def _savings_growth_prompt(p: dict) -> str:
    return f"""Savings Growth Analysis:
- Monthly savings : ₹{p.get('monthly_savings', 0):,.0f}
- Interest rate   : {p.get('interest_rate', 6)}%
- Target amount   : ₹{p.get('target_amount', 100000):,.0f}
- Time horizon    : {p.get('years', 5)} years
Show year-by-year balance, best Indian savings instruments,
tips to reach target faster."""


def _debt_repayment_prompt(p: dict) -> str:
    return f"""Debt Repayment Strategy:
- Total debt     : ₹{p.get('total_debt', 0):,.0f}
- Monthly payment: ₹{p.get('monthly_payment', 0):,.0f}
- Interest rate  : {p.get('interest_rate', 12)}% p.a.
- Extra payment  : ₹{p.get('extra_payment', 0):,.0f}/month
Provide payoff timeline, interest saved, avalanche vs snowball advice."""


def _investment_planning_prompt(p: dict) -> str:
    return f"""Investment Planning:
- Monthly investment: ₹{p.get('monthly_investment', 0):,.0f}
- Risk appetite     : {p.get('risk_appetite', 'moderate')}
- Horizon           : {p.get('years', 10)} years
- Goal              : {p.get('goal', 'wealth creation')}
Recommend asset allocation, Indian instruments (SIP/ELSS/NPS),
expected returns."""