import sys, os
#sys.path = list of folders Python searches for imports
#insert will  adds our project folder to that list
sys.path.insert(0, os.path.dirname(__file__) + "/..")

from flask import Flask, request, jsonify, render_template
from python.financial_advisor import explain_concept, generate_budget_plan
from python.scenarios import (
    run_savings_scenario,
    run_debt_scenario,
    run_investment_scenario,)
app = Flask(__name__, template_folder="templates", static_folder="static")
app.config["JSON_SORT_KEYS"] = False
# Frontend
@app.route("/")
def index():
    return render_template("index.html")
# API Routes
@app.route("/api/explain", methods=["POST"])
def api_explain():
    """
    POST /api/explain
    Body: { "concept": "compound interest" }
    Returns AI explanation of the financial concept.
    """
    data = request.get_json(silent=True) or {}
    concept = data.get("concept", "").strip()
    if not concept:
        return jsonify({"error": "Please provide a 'concept' field."}), 400
    explanation = explain_concept(concept)
    return jsonify({"concept": concept, "explanation": explanation})
@app.route("/api/budget", methods=["POST"])
def api_budget():
    """
    POST /api/budget
    Body: {
        "income": 50000,
        "expenses": { "Rent": 12000, "Food": 6000, "Transport": 3000 },
        "goals": "Build emergency fund and save for a car"
    }
    Returns personalised budget plan + 50/30/20 breakdown.
    """
    data = request.get_json(silent=True) or {}
    income = float(data.get("income", 0))
    expenses = {k: float(v) for k, v in data.get("expenses", {}).items()}
    goals = data.get("goals", "general financial stability")

    if income <= 0:
        return jsonify({"error": "Please provide a valid monthly income."}), 400

    plan = generate_budget_plan(income, expenses, goals)

    # Pre-computed numbers for charts / summary cards
    total_exp = sum(expenses.values())
    return jsonify({
        "income": income,
        "total_expenses": total_exp,
        "surplus": income - total_exp,
        "savings_rate": round((income - total_exp) / income * 100, 1),
        "rule_50_30_20": {
            "Needs (50%)": round(income * 0.50, 2),
            "Wants (30%)": round(income * 0.30, 2),
            "Savings (20%)": round(income * 0.20, 2),
        },
        "ai_plan": plan,
    })
@app.route("/api/scenario/savings", methods=["POST"])
def api_savings():
    """
    POST /api/scenario/savings
    Body: {
        "monthly_savings": 5000,
        "interest_rate": 7,
        "target_amount": 300000,
        "years": 5
    }
    """
    data = request.get_json(silent=True) or {}
    result = run_savings_scenario(
        monthly_savings=float(data.get("monthly_savings", 0)),
        interest_rate=float(data.get("interest_rate", 6)),
        target_amount=float(data.get("target_amount", 100000)),
        years=int(data.get("years", 5)),
    )
    return jsonify(result)
@app.route("/api/scenario/debt", methods=["POST"])
def api_debt():
    """
    POST /api/scenario/debt
    Body: {
        "total_debt": 200000,
        "monthly_payment": 5000,
        "interest_rate": 12,
        "extra_payment": 2000
    }
    """
    data = request.get_json(silent=True) or {}
    result = run_debt_scenario(
        total_debt=float(data.get("total_debt", 0)),
        monthly_payment=float(data.get("monthly_payment", 0)),
        interest_rate=float(data.get("interest_rate", 12)),
        extra_payment=float(data.get("extra_payment", 0)),
    )
    return jsonify(result)
@app.route("/api/scenario/investment", methods=["POST"])
def api_investment():
    """
    POST /api/scenario/investment
    Body: {
        "monthly_investment": 5000,
        "risk_appetite": "moderate",
        "years": 10,
        "goal": "retirement corpus"
    }
    """
    data = request.get_json(silent=True) or {}
    result = run_investment_scenario(
        monthly_investment=float(data.get("monthly_investment", 0)),
        risk_appetite=data.get("risk_appetite", "moderate"),
        years=int(data.get("years", 10)),
        goal=data.get("goal", "wealth creation"),
    )
    return jsonify(result)
# entry Point 
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)