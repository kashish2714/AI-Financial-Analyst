from flask import Flask, render_template, request, redirect
from extensions import db
from models import Holding, AnalysisHistory

from utils import get_stock_data
from ml.train_model import train_model
from ml.predict import predict_next

from llm import generate_ai_insight

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///finance.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


# ---------------- HOME ----------------
@app.route("/", methods=["GET", "POST"])
def home():

    stock = None
    ml_result = None

    if request.method == "POST":

        ticker = request.form.get("ticker")

        if ticker:

            try:
                ticker = ticker.upper()

                # 1. GET STOCK DATA
                stock = get_stock_data(ticker)

                # 2. SAVE HISTORY
                history = AnalysisHistory(
                    ticker=ticker,
                    analysis=f"{stock['company']} | Price: {stock['price']}"
                )
                db.session.add(history)
                db.session.commit()

                # 3. ML PREDICTION
                model, data = train_model(ticker)
                prediction, confidence = predict_next(data)

                prediction_text = "UP" if prediction == 1 else "DOWN"

                # 4. AI INSIGHT (LLM)
                ai_report = generate_ai_insight(
                    ticker,
                    prediction_text,
                    round(confidence * 100, 2),
                    "MA5, MA10, Return based signals"
                )

                ml_result = {
                    "prediction": prediction_text,
                    "confidence": round(confidence * 100, 2),
                    "ai_report": ai_report
                }

            except Exception as e:
                print("ERROR:", e)
                stock = None
                ml_result = None

    return render_template(
        "index.html",
        stock=stock,
        ml_result=ml_result
    )


# ---------------- PORTFOLIO ----------------
@app.route("/portfolio")
def portfolio():

    holdings = Holding.query.all()

    data = []
    total = 0

    for h in holdings:

        stock = get_stock_data(h.ticker)
        price = stock["price"]

        value = price * h.quantity if isinstance(price, (int, float)) else 0
        total += value

        data.append({
            "ticker": h.ticker,
            "quantity": h.quantity,
            "price": price,
            "value": round(value, 2)
        })

    return render_template(
        "portfolio.html",
        holdings=data,
        total_value=round(total, 2)
    )


# ---------------- HISTORY ----------------
@app.route("/history")
def history():

    items = AnalysisHistory.query.order_by(
        AnalysisHistory.created_at.desc()
    ).all()

    return render_template("history.html", items=items)


# ---------------- ADD PORTFOLIO ----------------
@app.route("/api/portfolio", methods=["POST"])
def add_portfolio():

    data = request.get_json()

    ticker = data["ticker"].upper()
    quantity = float(data["quantity"])

    holding = Holding.query.filter_by(ticker=ticker).first()

    if holding:
        holding.quantity = quantity
    else:
        holding = Holding(ticker=ticker, quantity=quantity)
        db.session.add(holding)

    db.session.commit()

    return {"message": "saved"}


# ---------------- DELETE ----------------
@app.route("/delete/<ticker>")
def delete_stock(ticker):

    holding = Holding.query.filter_by(ticker=ticker).first()

    if holding:
        db.session.delete(holding)
        db.session.commit()

    return redirect("/portfolio")


# ---------------- INIT DB ----------------
with app.app_context():
    db.create_all()


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)