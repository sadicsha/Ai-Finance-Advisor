from dataclasses import dataclass, field #create a clean data container
from typing import Dict, List, Tuple


@dataclass
class BudgetSummary:
    income: float #your monthly salary
    expenses: Dict[str, float] #category & amount
    goals: str # what you want to achieve 

    @property
    def total_expenses(self) -> float: 
        return sum(self.expenses.values())# adds up all expense amounts automatically

    @property
    def surplus(self) -> float:
        return self.income - self.total_expenses

    @property
    def savings_rate(self) -> float:
        return (self.surplus / self.income * 100) if self.income else 0 #what % of income you are saving

    @property
    def expense_breakdown(self) -> List[Tuple[str, float, float]]:
        """Returns list of (category, amount, % of income)."""
        return [
            (cat, amt, round(amt / self.income * 100, 1))
            for cat, amt in self.expenses.items()# Returns each expense with its % of income
        ]

# The 50/30/20 budgeting rule:50% for Needs, 30% for Wants, 20% for Savings
    def rule_50_30_20(self) -> Dict[str, float]:
        """Classic 50/30/20 budget rule allocations."""
        return {
            "Needs (50%)": round(self.income * 0.50, 2),
            "Wants (30%)": round(self.income * 0.30, 2),
            "Savings / Debt (20%)": round(self.income * 0.20, 2),
        }

#Converts all budget data into a dictionary so Flask can send it to the browser as JSON
    def to_dict(self) -> dict:
        return {
            "income": self.income,
            "expenses": self.expenses,
            "total_expenses": self.total_expenses,
            "surplus": self.surplus,
            "savings_rate": round(self.savings_rate, 2),
            "rule_50_30_20": self.rule_50_30_20(),
        }

#Calculate compound savings growth year by year. Calculates how your savings grow with interest month by month
#Returns a list of {year, balance, interest_earned} dicts.
#Inner loop runs 12 times (once per month)
#Each month: add savings → apply interest

def compound_savings(
    monthly_amount: float,
    annual_rate: float,
    years: int,
) -> List[Dict]:
    monthly_rate = annual_rate / 100 / 12 #converts yearly % to monthly
    balance = 0.0
    records = []
    for year in range(1, years + 1):
        for _ in range(12):
            balance += monthly_amount
            balance *= 1 + monthly_rate
        total_deposited = monthly_amount * 12 * year
        records.append({
            "year": year,
            "balance": round(balance, 2),
            "total_deposited": round(total_deposited, 2),
            "interest_earned": round(balance - total_deposited, 2),
        })
    return records

#Calculates how many months to pay off a loan
#Each month:Calculate interest on remaining balance, Subtract your payment then Count the month. Keeps running until balance reaches zero
def debt_payoff_months(
    principal: float,
    monthly_payment: float,
    annual_rate: float,
) -> Tuple[int, float]:
    if monthly_payment <= 0:
        return (0, 0.0)
    monthly_rate = annual_rate / 100 / 12
    balance = principal
    months = 0
    total_paid = 0.0
    while balance > 0 and months < 600:   # cap at 50 years
        interest = balance * monthly_rate
        principal_paid = min(monthly_payment - interest, balance)
        if principal_paid <= 0:
            # Payment doesn't cover interest — debt is growing
            return (-1, -1.0)
        balance -= principal_paid
        total_paid += monthly_payment if balance > 0 else (principal_paid + interest)
        months += 1
    return (months, round(total_paid - principal, 2))

# Projects how much your investment grows over time, Reuses compound_savings function
def investment_projection(
    monthly_investment: float,
    annual_cagr: float,
    years: int,
) -> Dict:
    """
    Project SIP / monthly investment value using CAGR.
    """
    records = compound_savings(monthly_investment, annual_cagr, years)
    final = records[-1] if records else {}#gets the last year's final value
    return {
        "monthly_investment": monthly_investment,
        "annual_cagr": annual_cagr,
        "years": years,
        "projected_value": final.get("balance", 0),
        "total_invested": final.get("total_deposited", 0),
        "wealth_created": final.get("interest_earned", 0),
        "year_by_year": records,
    }# Returns total value, amount invested, and profit earned
