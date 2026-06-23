import pandas as pd
import numpy as np
import yfinance as yf


def compute_rsi(series, period=14):

    delta = series.diff()

    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()

    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))

    return rsi


def create_features(ticker):

    df = yf.download(ticker, period="6mo", interval="1d")
    df = df.dropna()

    # Basic features
    df["Return"] = df["Close"].pct_change()
    df["MA5"] = df["Close"].rolling(5).mean()
    df["MA10"] = df["Close"].rolling(10).mean()

    # RSI (MANUAL 🔥)
    df["RSI"] = compute_rsi(df["Close"], 14)

    # Volatility
    df["Volatility"] = df["Return"].rolling(10).std()

    df = df.dropna()

    features = df[[
        "Return",
        "MA5",
        "MA10",
        "RSI",
        "Volatility"
    ]]

    return df, features