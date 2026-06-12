import yfinance as yf

def get_stock_data(ticker):

    stock = yf.Ticker(ticker)
    info = stock.info

    return {
        "ticker": ticker.upper(),
        "company": info.get("shortName", "N/A"),
        "price": info.get("currentPrice", 0),
        "pe_ratio": info.get("trailingPE", "N/A"),
        "beta": info.get("beta", "N/A"),
        "sector": info.get("sector", "N/A")
    }