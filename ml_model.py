import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier


def train_model(ticker):

    data = yf.download(ticker, period="6mo", interval="1d")

    if data is None or data.empty:
        raise Exception("No data returned from Yahoo")

    data = data.copy()

    data["Return"] = data["Close"].pct_change()
    data["MA5"] = data["Close"].rolling(5).mean()
    data["MA10"] = data["Close"].rolling(10).mean()

    data = data.dropna()

    data["Target"] = (data["Close"].shift(-1) > data["Close"]).astype(int)

    features = ["Return", "MA5", "MA10"]

    X = data[features][:-1]
    y = data["Target"][:-1]

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    return model, data


def predict_next(model, data):

    latest = data[["Return", "MA5", "MA10"]].iloc[-1]

    # 🔥 FORCE PURE 2D NUMPY ARRAY (this is the real fix)
    features = np.array([
        latest["Return"],
        latest["MA5"],
        latest["MA10"]
    ]).reshape(1, -1)

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][prediction]

    return prediction, float(probability)