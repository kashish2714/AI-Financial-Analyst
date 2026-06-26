# AI Financial Analyst Web Application

## Overview

An AI-powered financial analysis web application that combines machine learning, technical indicators, and LLM-generated insights to predict short-term stock price movement and generate analyst-style financial reports.

---

## Features

* Fetch real-time stock market data using Yahoo Finance (`yfinance`)
* Predict next-day stock movement using a Random Forest classifier
* Generate AI-powered financial insights using the Groq LLM
* Compute technical indicators including:

  * Relative Strength Index (RSI)
  * Moving Average Convergence Divergence (MACD)
  * 5-day and 10-day Moving Averages
  * Volatility
* Portfolio management system
* Analysis history tracking
* SQLite database integration using SQLAlchemy

---

## Machine Learning Model

**Model:** Random Forest Classifier

**Learning Type:** Supervised Classification

### Features Used

* Daily Return
* 5-Day Moving Average
* 10-Day Moving Average
* RSI
* MACD
* MACD Signal
* Volatility

### Prediction Output

* Next-day stock movement (UP / DOWN)
* Prediction confidence score

---

## Model Performance

| Metric            | Value      |
| ----------------- | ---------- |
| Training Accuracy | ~0.85      |
| Test Accuracy     | ~0.47–0.60 |
| F1 Score          | ~0.55–0.58 |

> Stock markets are highly stochastic; these results are consistent with realistic short-term price prediction tasks.

---

## AI Component

The application uses the Groq LLM to generate:

* Market interpretation
* Explanation of model predictions
* Risk analysis
* Analyst-style financial summaries

This improves the interpretability of machine learning predictions by providing natural language explanations.

---

## Tech Stack

* Python
* Flask
* Scikit-learn
* Pandas
* NumPy
* yfinance
* ta
* SQLAlchemy
* Groq API
* HTML
* Jinja2

---

## Project Structure

```text
AI-Financial-Analyst/
│
├── app.py
├── ml/
│   ├── train_model.py
│   └── features.py
├── models/
│   └── model.pkl
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── portfolio.html
│   └── history.html
├── extensions.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/kashish2714/AI-Financial-Analyst.git
```

Navigate to the project directory

```bash
cd AI-Financial-Analyst
```

Install the required packages

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your Groq API key

```env
GROQ_API_KEY=your_groq_api_key_here
```

Run the application

```bash
python app.py
```

Open the application in your browser:

```text
http://127.0.0.1:5000
```
