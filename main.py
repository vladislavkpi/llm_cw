# імпортуємо бібліотеки
from openai import OpenAI
import os
from fastapi import FastAPI
from nixtla import NixtlaClient
import yfinance as yf
import pandas as pd
from pydantic import BaseModel
import nest_asyncio
import uvicorn
import requests
import json
#from google.colab import userdata #треба у випадку роботи з колабом
from app.forecast import predict_stock_price
from app.forecast import get_time_series_data
from app.analysis import generate_analysis

# ініціюємо АПІ
app = FastAPI()

class StockRequest(BaseModel):
    ticker: str

@app.get("/")
def home():
    return {"message": "Welcome to the Financial Analysis API"}

# Основна функція для генерації відповіді по різних фінансових параметрах та прогнозу
@app.post("/analyze/")
def analyze_stock(request: StockRequest):
    ticker = request.ticker.upper()
    stock = yf.Ticker(ticker)
    company_name = stock.info.get('longName', ticker)
    
    # Fetch financial data
    financials = stock.financials.T
    financials = financials[:1]
    balance_sheet = stock.balance_sheet.T
    balance_sheet = balance_sheet[:1]
    cash_flow = stock.cashflow.T
    cash_flow = cash_flow[:1]
    price_data = get_time_series_data(ticker)
    stock_forecast = predict_stock_price(price_data)
    # Extract key financial metrics
    try:
        roe = float((financials['Net Income'] / balance_sheet['Common Stock Equity']) * 100)
        roa = float((financials['Net Income'] / balance_sheet['Total Assets']) * 100)
        gross_margin = float((financials['Gross Profit'] / financials['Total Revenue']) * 100)
    except KeyError:
        roe, roa, gross_margin = None, None, None
    
    try:
        debt_to_equity = float((balance_sheet['Total Debt'] / balance_sheet['Common Stock Equity']))
        interest_coverage = float((financials['EBIT'] / financials['Interest Expense']))
    except KeyError:
        debt_to_equity, interest_coverage = None, None
    
    try:
        current_ratio = float((balance_sheet['Current Assets'] / balance_sheet['Current Liabilities']))
        quick_ratio = float(((balance_sheet['Current Assets'] - balance_sheet['Inventory']) / balance_sheet['Current Liabilities']))
        cash_reserves = float(cash_flow['Cash Flow From Continuing Operating Activities'])
    except KeyError:
        current_ratio, quick_ratio, cash_reserves = None, None, None
          
    return {
        "company": company_name,
        "financials": {
            #"profitability": generate_analysis("Return on Equity", roe, company_name),
            "profitability": generate_analysis("Return on Assets", roa, company_name),
            #"profitability": generate_analysis("Gross margin", gross_margin, company_name),
            "indebtedness": generate_analysis("Debt to equity", debt_to_equity, company_name),
            #"indebtedness": generate_analysis("Interest coverage", interest_coverage, company_name),
            "liquidity": generate_analysis("Current ratio", current_ratio, company_name),
            #"liquidity": generate_analysis("Quick ratio", quick_ratio, company_name),
            #"profit_margin": generate_analysis("Cash reserves", cash_reserves, company_name)
            "stock_price_forecast (3 month)": stock_forecast
        }
    }

### Запускаємо сервер FastAPI у фоновому режимі ###
nest_asyncio.apply()
uvicorn.run(app, host="127.0.0.1", port=8000)

### для Colab: ###
nest_asyncio.apply()
from pyngrok import ngrok
ngrok.set_auth_token(userdata.get('ngrok'))

public_url = ngrok.connect(8000).public_url
print(f"Public URL: {public_url}")

# Запускаємо Uvicorn
uvicorn.run(app, host="127.0.0.1", port=8000)
