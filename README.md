# AI Financial Analyst Web App

## 📊 Overview
This project is a full-stack AI-powered financial analysis web application built using Flask. It fetches real-time stock data, manages a user portfolio, and uses Machine Learning to predict short-term stock movement.

---

## 🚀 Features

- Real-time stock data using Yahoo Finance API (yfinance)
- Stock analysis dashboard (price, PE ratio, beta, sector)
- Portfolio management system (add/delete stocks)
- SQLite database integration using SQLAlchemy
- ML-based stock direction prediction (UP / DOWN)
- Analysis history tracking

---

## 🧠 Machine Learning Model

- Model: Random Forest Classifier
- Type: Supervised Learning (Classification)
- Features used:
  - Daily return
  - 5-day moving average
  - 10-day moving average
- Output:
  - Stock movement prediction (UP / DOWN)
  - Confidence score

Note: This model is for educational purposes and not for financial trading.

---

## 🛠 Tech Stack

- Python
- Flask
- SQLAlchemy
- Scikit-learn
- Pandas
- NumPy
- yfinance
- HTML / Jinja2

---

## 📁 Project Structure

AI-Financial-Analyst/
│
├── app.py
├── ml_model.py
├── utils.py
├── models.py
├── extensions.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── portfolio.html
│   └── history.html
│
├── requirements.txt
└── README.md

---

## ▶️ How to Run

pip install -r requirements.txt
python app.py

Then open:
http://127.0.0.1:5000

---

## 🎯 What This Project Demonstrates

- End-to-end ML pipeline
- Feature engineering from financial data
- Integration of ML with web development
- Database design and management
- API integration (Yahoo Finance)
- Full-stack project architecture

---

## ⚠️ Disclaimer
This project is for educational purposes only and does not provide financial advice or real trading recommendations.