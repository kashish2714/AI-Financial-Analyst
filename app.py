from flask import Flask, render_template, request, redirect
from utils import get_stock_data
from extensions import db
from models import Holding, AnalysisHistory

# ML
from ml_model import train_model, predict_next

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
                # STOCK DATA
                stock = get_stock_data(ticker)

                # SAVE HISTORY
                history = AnalysisHistory(
                    ticker=ticker.upper(),
                    analysis=f"{stock['company']} | Price: {stock['price']}"
                )

                db.session.add(history)
                db.session.commit()

                # ML MODEL
                model, data = train_model(ticker)
                prediction, confidence = predict_next(model, data)

                ml_result = {
                    "prediction": "UP" if prediction == 1 else "DOWN",
                    "confidence": round(confidence * 100, 2)
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