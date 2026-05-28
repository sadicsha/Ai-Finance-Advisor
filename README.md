# 💰 AI Financial Literacy Advisor

> An intelligent web-based personal finance chatbot powered by **Meta LLaMA 3** via **Hugging Face API**, built with **Python Flask** backend and interactive **HTML/CSS/JavaScript** frontend.

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-green?logo=flask)
![HuggingFace](https://img.shields.io/badge/HuggingFace-LLaMA3-orange?logo=huggingface)
![License](https://img.shields.io/badge/License-MIT-purple)

---

## 📌 About the Project

The **AI Financial Literacy Advisor** is a web application developed as part of the **SmartBridge Educational Services Pvt. Ltd., Hyderabad** internship program. It addresses the widespread challenge of financial illiteracy in India by providing an AI-powered platform that:

- Explains complex financial concepts in **plain, simple language**
- Generates **personalised monthly budget plans** based on real income and expenses
- Delivers **scenario-based financial insights** for savings, debt, and investment planning
- Formats all values in **Indian Rupees (₹)** for local relevance

---

## 🚀 Features

| Feature | Description |
|---|---|
| 📚 **Explain Concept** | Type any financial term and get a beginner-friendly AI explanation |
| 📊 **Budget Planner** | Enter income & expenses to get a personalised 50/30/20 budget plan |
| 🏦 **Savings Growth** | Calculate compound savings growth year by year |
| 💳 **Debt Repayment** | Compare payoff timelines with and without extra payments |
| 📈 **Investment Planning** | Project SIP/mutual fund portfolio value based on risk appetite |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Language** | Python 3.12 |
| **Backend** | Flask Web Framework |
| **AI Model** | meta-llama/Meta-Llama-3-8B-Instruct |
| **AI API** | Hugging Face Inference API (Free Tier) |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript |
| **Charts** | Chart.js (CDN) |
| **Currency** | Indian Rupee (₹) — Intl.NumberFormat('en-IN') |

---

## 📁 Project Structure

```
AI-Finance-Advisor/
│
├── app.py                      # Flask entry point + all API routes
│
├── python/
│   ├── __init__.py             # Package initializer
│   ├── financial_advisor.py    # AI integration — Hugging Face + LLaMA 3
│   ├── budget_calculator.py    # Pure math — savings, debt, investment
│   └── scenarios.py            # Bridge — combines math + AI
│
├── templates/
│   └── index.html              # Main frontend UI — 3 tab interface
│
├── static/
│   └── style.css               # Global stylesheet
│
└── README.md
```

---

## ⚙️ Installation & Setup

### Step 1 — Clone the Repository
```bash
git clone https://github.com/YourUsername/AI-Finance-Advisor.git
cd AI-Finance-Advisor
```

### Step 2 — Install Required Libraries
```bash
pip install flask
pip install huggingface_hub
```

### Step 3 — Configure Hugging Face API Key
1. Go to https://huggingface.co/settings/tokens
2. Create a free account and generate a **Read** token
3. Open `python/financial_advisor.py`
4. Replace the API key:
```python
HF_API_KEY = "hf_xxxxxxxxxxxxxxxxxxxx"   # paste your token here
```

### Step 4 — Run the Application
```bash
py app.py
```

### Step 5 — Open in Browser
```
http://127.0.0.1:5000
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Serves the main frontend HTML page |
| POST | `/api/explain` | Returns AI explanation of a financial concept |
| POST | `/api/budget` | Returns personalised budget plan + summary |
| POST | `/api/scenario/savings` | Returns savings growth projection + AI insight |
| POST | `/api/scenario/debt` | Returns debt payoff comparison + AI insight |
| POST | `/api/scenario/investment` | Returns investment projection + AI insight |

---

## 💡 How It Works

```
User fills form in browser
          ↓
JavaScript sends POST request with JSON data
          ↓
Flask backend receives and validates input
          ↓
scenarios.py combines:
    ├── budget_calculator.py  (pure math calculations)
    └── financial_advisor.py  (AI prompt + Hugging Face API call)
          ↓
LLaMA 3 model generates financial advice
          ↓
Flask returns JSON response
          ↓
Browser displays AI text + INR formatted numbers ✅
```

---

## 📸 Application Screenshots

### Explain Concept Tab
> Users type any financial term or click quick chips to get a plain-language AI explanation

### Budget Planner Tab
> Users enter income and expenses to receive a personalised budget plan with stat cards

### Scenarios Tab
> Three scenario tools — Savings Growth, Debt Repayment, Investment Planning

---

## 📋 Prerequisites

| Requirement | Link |
|---|---|
| Python 3.12+ | https://www.python.org/downloads/ |
| Flask | https://flask.palletsprojects.com/ |
| Hugging Face API | https://huggingface.co/docs/api-inference/ |
| LLaMA 3 Model | https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct |
| Hugging Face Hub | https://huggingface.co/docs/huggingface_hub/ |
| HTML/CSS/JS | https://developer.mozilla.org/en-US/docs/Web |
| Chart.js | https://www.chartjs.org/docs/latest/ |

---

## 🧠 AI Model Details

- **Model:** `meta-llama/Meta-Llama-3-8B-Instruct`
- **Provider:** Hugging Face Inference API
- **Parameters:** 8 Billion
- **Type:** Instruction-tuned — optimised for following directions
- **Cost:** Free tier — no credit card required
- **Temperature:** 0.7 — balanced creativity and accuracy
- **Max Tokens:** 1500 — detailed responses without being too long

---

## 🇮🇳 India-Specific Features

- All monetary values formatted in **₹ Indian Rupees**
- Recommends Indian savings instruments: **FD, RD, PPF, NSC**
- Suggests Indian investment options: **SIP, ELSS, NPS, Index Funds**
- CAGR estimates based on **Indian market historical returns**
- Debt strategies relevant to **Indian loan and EMI structures**

---

## ⚠️ Important Notes

- This application runs **locally** on your machine
- You must run `py app.py` **every time** before opening the browser
- The Hugging Face free tier may have **response times of 3-8 seconds**
- Keep PowerShell/terminal **open** while using the app
- To stop the server press **CTRL + C**

---

## 🔮 Future Enhancements

- [ ] Live NSE/BSE stock market data integration
- [ ] User authentication and personalised history
- [ ] Mobile application (React Native)
- [ ] Voice-based queries (Web Speech API)
- [ ] Hindi and Telugu language support
- [ ] Cloud deployment (Render / Railway)
- [ ] Indian banking API integration

---

## 👨‍💻 Developed By

**Sadicsha**
SmartBridge Educational Services Pvt. Ltd., Hyderabad
AI Financial Literacy Advisor — Internship Project

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use and modify for educational purposes.

---

> *Made with ❤️ to make financial literacy accessible to every Indian* 🇮🇳
