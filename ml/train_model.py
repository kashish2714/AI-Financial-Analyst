import numpy as np
import joblib
import yfinance as yf
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
import ta


def create_dataset(df):

    df = df.copy()

    # Features
    df["return"] = df["Close"].pct_change()
    df["ma5"] = df["Close"].rolling(5).mean()
    df["ma10"] = df["Close"].rolling(10).mean()
    df["volatility"] = df["return"].rolling(5).std()

    close = df["Close"].squeeze()

    df["rsi"] = ta.momentum.RSIIndicator(close, window=14).rsi().values
    macd = ta.trend.MACD(close)

    df["macd"] = macd.macd().values
    df["macd_signal"] = macd.macd_signal().values

    # 🔥 TARGET INSIDE SAME FRAME (IMPORTANT FIX)
    df["target"] = (df["Close"].shift(-1) > df["Close"]).astype(int)

    df = df.dropna()

    X = df[[
        "return",
        "ma5",
        "ma10",
        "volatility",
        "rsi",
        "macd",
        "macd_signal"
    ]].values

    y = df["target"].values

    return X, y


def train_model():

    print("🚀 Training started...")

    tickers = ["AAPL", "TSLA", "MSFT"]

    X_all = []
    y_all = []

    for ticker in tickers:

        print(f"📊 Processing {ticker}")

        df = yf.download(ticker, period="1y", interval="1d")

        if df.empty:
            continue

        X, y = create_dataset(df)

        if len(X) == 0:
            continue

        X_all.append(X)
        y_all.append(y)

    X = np.vstack(X_all)
    y = np.hstack(y_all)

    print(f"📦 Dataset size: {X.shape}, {y.shape}")

    split = int(len(X) * 0.8)

    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]

    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=6,
        min_samples_leaf=4,
        random_state=42
    )

    model.fit(X_train, y_train)

    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)

    print("\n📊 RESULTS")
    print("Train Accuracy:", round(accuracy_score(y_train, train_pred), 3))
    print("Test Accuracy:", round(accuracy_score(y_test, test_pred), 3))
    print("F1 Score:", round(f1_score(y_test, test_pred), 3))

    joblib.dump(model, "models/model.pkl")

    print("\n💾 Model saved successfully!")


if __name__ == "__main__":
    train_model()