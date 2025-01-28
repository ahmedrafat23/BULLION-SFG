from flask import Flask, render_template, request, jsonify
import os
import requests
from dotenv import load_dotenv

# Explicitly load the .env file
dotenv_path = "/home/rafat/BULLION-SFG/.env"
load_dotenv(dotenv_path)

app = Flask(__name__)

# Load API keys from environment variables
METALS_API_KEY = os.getenv("METALS_API_KEY")
STOCKS_API_KEY = os.getenv("STOCKS_API_KEY")
FINANCE_API_KEY = os.getenv("FINANCE_API_KEY")

if not all([METALS_API_KEY, STOCKS_API_KEY, FINANCE_API_KEY]):
    raise ValueError("API keys are missing. Please set them in the environment.")

# Debugging: Print API keys to ensure they are loaded correctly
print("METALS_API_KEY:", METALS_API_KEY)
print("STOCKS_API_KEY:", STOCKS_API_KEY)
print("FINANCE_API_KEY:", FINANCE_API_KEY)

def fetch_metal_data():
    url = f"https://metals-api.com/api/latest?access_key={METALS_API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data.get("rates", {})

def fetch_stock_data():
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={STOCKS_API_KEY}"
    response = requests.get(url)
    return response.json().get("stocks", [])

def currency_converter():
    amount = float(request.args.get("amount", 0))
    currency = request.args.get("currency", "USD")
    url = f"https://api.currencylayer.com/live?access_key={FINANCE_API_KEY}&amount={amount}&currency={currency}"
    response = requests.get(url)
    data = response.json()
    return jsonify({"convertedAmount": data.get("result", 0)})

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/metals")
def metals():
    metals_data = fetch_metal_data()
    return render_template("metals.html", metals=metals_data)

@app.route("/stocks")
def stocks():
    stocks_data = fetch_stock_data()
    return render_template("stocks.html", stocks=stocks_data)

@app.route("/currency", methods=["GET"])
def currency():
    currency_data = currency_converter()
    return render_template("currency.html", currencies=currency_data)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, jsonify
import os
import requests

app = Flask(__name__)

# Load API keys from environment variables
METALS_API_KEY = os.getenv("METALS_API_KEY")
STOCKS_API_KEY = os.getenv("STOCKS_API_KEY")
FINANCE_API_KEY = os.getenv("FINANCE_API_KEY")

if not all([METALS_API_KEY, STOCKS_API_KEY, FINANCE_API_KEY]):
    raise ValueError("API keys are missing. Please set them in the environment.")

def fetch_metal_data():
    url = f"https://metals-api.com/api/latest?access_key={METALS_API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data.get("rates", {})

def fetch_stock_data():
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={STOCKS_API_KEY}"
    response = requests.get(url)
    return response.json().get("stocks", [])


def currency_converter():
    amount = float(request.args.get("amount", 0))
    currency = request.args.get("currency", "USD")
    url = f"https://api.currencylayer.com/live?access_key={FINANCE_API_KEY}&amount={amount}&currency={currency}"
    response = requests.get(url)
    data = response.json()
    return jsonify({"convertedAmount": data.get("result", 0)})

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/metals")
def metals():
    metals_data = fetch_metal_data()
    return render_template("metals.html", metals=metals_data)

@app.route("/stocks")
def stocks():
    stocks_data = fetch_stock_data()
    return render_template("stocks.html", stocks=stocks_data)

@app.route("/currency", methods=["GET"])
def currency():
    currency_data = currency_converter()
    return render_template("currency.html", currencies=currency_data)

if __name__ == "__main__":
    app.run(debug=True)
