import numpy as np
import joblib

# load model ONCE
model = joblib.load("models/model.pkl")


def predict_next(data):
    latest = data[["Return", "MA5", "MA10"]].iloc[-1]

    X = np.array([
        latest["Return"],
        latest["MA5"],
        latest["MA10"]
    ]).reshape(1, -1)

    pred = model.predict(X)[0]
    prob = model.predict_proba(X)[0][pred]

    return pred, float(prob)