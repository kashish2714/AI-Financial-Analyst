# 📊 AI Financial Analyst Web App

## 🚀 Overview
An AI-powered financial analysis web application that combines **Machine Learning, Technical Indicators, and LLM-based insights** to predict short-term stock movement and generate analyst-style reports.

---

## ✨ Features

- 📈 Real-time stock data using Yahoo Finance (yfinance)
- 🤖 Machine Learning-based stock prediction (UP / DOWN)
- 🧠 AI Analyst Report using LLM (Groq API)
- 📊 Technical Indicators:
  - RSI (Relative Strength Index)
  - MACD (Moving Average Convergence Divergence)
  - Moving Averages (MA5, MA10)
  - Volatility analysis
- 💼 Portfolio management system
- 🗂 SQLite database (SQLAlchemy)
- 📜 Analysis history tracking

---

## 🧠 Machine Learning Model

- Model: Random Forest Classifier
- Type: Supervised Learning (Classification)

### 📊 Features Used:
- Daily return
- Moving averages (5-day, 10-day)
- RSI
- MACD
- MACD Signal
- Volatility

### 🎯 Output:
- Stock direction prediction (UP / DOWN)
- Confidence score

---

## 📊 Model Performance

- Train Accuracy: ~0.85
- Test Accuracy: ~0.47–0.60
- F1 Score: ~0.55–0.58

> Note: Stock markets are highly stochastic; these results are realistic for short-term prediction models.

---

## 🧠 AI Component

The system uses an LLM (Groq API) to generate:

- Market explanation
- Reason behind prediction
- Risk analysis
- Analyst-style report

This makes the system interpretable, not just predictive.

---

## 🛠 Tech Stack

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- yfinance
- ta (technical indicators)
- SQLAlchemy
- Groq LLM API
- HTML / Jinja2

---

## 📁 Project Structure
AI-Financial-Analyst/
│
├── app.py
├── ml/
│ ├── train_model.py
│ ├── features.py
│
├── models/
│ └── model.pkl
│
├── templates/
│ ├── base.html
│ ├── index.html
│ ├── portfolio.html
│ └── history.html
│
├── extensions.py
├── requirements.txt
└── README.md


---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python app.py

Then open:

http://127.0.0.1:5000
