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

# ініціюємо АПІ
app = FastAPI()

class StockRequest(BaseModel):
    ticker: str

@app.get("/")
def home():
    return {"message": "Welcome to the Financial Analysis API"}

# пропишемо ключі, якщо працюємо через Колаб
client = OpenAI(
  api_key=userdata.get('api_key')
)
nixtla_client = NixtlaClient(
    api_key = userdata.get('TIMEGPT_API_KEY')
)

# пропишемо ключі, якщо працюємо через Python
client = OpenAI(
  api_key=OPENAI_API_KEY
)
nixtla_client = NixtlaClient(
    api_key = TIMEGPT_API_KEY
)

