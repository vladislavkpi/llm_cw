import os
import yfinance as yf
import pandas as pd
import requests

# пропишемо ключі, якщо працюємо через Колаб
nixtla_client = NixtlaClient(
    api_key = userdata.get('TIMEGPT_API_KEY')
)
nixtla_client = NixtlaClient(
    api_key = TIMEGPT_API_KEY
)

# Функція для отримання історичних даних та підготовки часових рядів

def get_time_series_data(ticker):
    stock = yf.Ticker(ticker)
    price_data = stock.history(period="2y", interval="1mo")[['Close']]
    price_data.reset_index(inplace=True)
    price_data.rename(columns={"Date": "date", "Close": "stock_price"}, inplace=True)
    # Перетворення стовпця дати у формат datetime
    price_data["date"] = pd.to_datetime(price_data["date"])
    return price_data

# Функція для прогнозування ціни акцій

def predict_stock_price(df):
    if df is None or df.empty:
        return {"error": "Not enough data for forecasting"}
    
    forecast = nixtla_client.forecast(
        df=df,
        freq='MS',
        time_col='date',
        target_col='stock_price',
        h=3,
        #level=[80, 90]
    )
    return float(forecast[2:3]['TimeGPT'])
