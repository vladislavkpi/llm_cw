"""
Параметри:
block_name (str): Назва фінансового показника (наприклад, "profitability").
value (float): Значення фінансового показника.
company_name (str): Назва компанії.

Повертає:
str: Структурований фінансовий аналіз у текстовому форматі.
"""
from openai import OpenAI
import os

# пропишемо ключі, якщо працюємо через Колаб
client = OpenAI(
  api_key=userdata.get('api_key')
)
nixtla_client = NixtlaClient(
    api_key = userdata.get('TIMEGPT_API_KEY')
)

def generate_analysis(block_name, value, company_name):
    prompt = (
        f"Provide a structured financial analysis of {block_name} for {company_name} with a value of {value}. "
        "Explain whether the value is good or bad, describe the recent trend (increasing, stable, or decreasing), "
        "compare it with the industry average, and provide insights. Keep the response clear and concise."
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "You are a financial analyst."},
                  {"role": "user", "content": prompt}],
        max_tokens=200,
        temperature=0.5,
        top_p=0.9
    )

    return response.choices[0].message.content.strip()
