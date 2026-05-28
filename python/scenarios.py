from python.budget_calculator import (
    compound_savings,
    debt_payoff_months,
    investment_projection,
)
from python.financial_advisor import analyse_scenario
def run_savings_scenario(
    monthly_savings: float, #how much you save per month
    interest_rate: float, #bank interest rate
    target_amount: float, #how much you want to save
    years: int, #how long you will save
) -> dict:
    """Full savings-growth scenario: numbers + AI narrative."""
    projections = compound_savings(monthly_savings, interest_rate, years)#Gets year-by-year numbers of how savings grow
    ai_insight = analyse_scenario(
        "savings_growth",
        {
            "monthly_savings": monthly_savings,
            "interest_rate": interest_rate,
            "target_amount": target_amount,
            "years": years, #Sends user's numbers to AI, it generates a detailed written analysis and tips
        },
    )
    return {
        "type": "savings_growth",
        "projections": projections, # numbers from math calculation
        "ai_insight": ai_insight, # written advice from AI
    }
def run_debt_scenario(
    total_debt: float,
    monthly_payment: float,
    interest_rate: float,
    extra_payment: float = 0,
) -> dict:
    """Debt repayment scenario: payoff timeline + AI narrative."""
    months_base, interest_base = debt_payoff_months(
        total_debt, monthly_payment, interest_rate
    )
    #Calculates payoff time with extra payment
    months_extra, interest_extra = debt_payoff_months(
        total_debt, monthly_payment + extra_payment, interest_rate
    )
    ai_insight = analyse_scenario(
        "debt_repayment",
        {
            "total_debt": total_debt,
            "monthly_payment": monthly_payment,
            "interest_rate": interest_rate,
            "extra_payment": extra_payment,
        },
    )
    return {
        "type": "debt_repayment",
        "base": {"months": months_base, "interest_paid": interest_base},
        "with_extra": {"months": months_extra, "interest_paid": interest_extra},
        "months_saved": max(months_base - months_extra, 0),
        "interest_saved": max(interest_base - interest_extra, 0),
        "ai_insight": ai_insight,
    }


def run_investment_scenario(
    monthly_investment: float,
    risk_appetite: str,
    years: int,
    goal: str,
) -> dict:
    """Investment planning scenario with CAGR by risk level + AI narrative."""
    cagr_map = {"low": 7.0, "moderate": 11.0, "high": 15.0}
    cagr = cagr_map.get(risk_appetite.lower(), 11.0)
    projection = investment_projection(monthly_investment, cagr, years)
    ai_insight = analyse_scenario(
        "investment_planning",
        {
            "monthly_investment": monthly_investment,
            "risk_appetite": risk_appetite,
            "years": years,
            "goal": goal,
        },
    )
    return {
        "type": "investment_planning",
        "assumed_cagr": cagr,
        "projection": projection,
        "ai_insight": ai_insight,
    }
