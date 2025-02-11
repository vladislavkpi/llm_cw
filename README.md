# Financial Analysis API

## 📌 Project Goals
This project aims to provide **automated financial analysis** and **stock price forecasting** using a combination of:
- **TimeGPT** for time-series forecasting (3-month stock price prediction).
- **GPT-4o-mini** for textual financial analysis.
- **Yahoo Finance API** for fetching financial data.
- **FastAPI** for API deployment.

The API is designed for investors, analysts, and researchers who need **quick insights** into company financials and stock price trends.

---

## 🚀 How to Run the Project
### **1. Install Dependencies**
Ensure you have **Python 3.8+** installed, then run:
```bash
pip install fastapi uvicorn yfinance openai pandas requests
pip install nixtla
```

### **2. Set Up API Keys**
This project requires API keys for:
- **OpenAI API** (`GPT-4o-mini`): Sign up at [OpenAI](https://platform.openai.com/) and set up an API key.
- **TimeGPT API** (for stock price forecasting): Sign up at [Nixtla](https://nixtla.io/) and obtain an API key.

Set these in your environment variables:
```bash
export OPENAI_API_KEY='your_openai_api_key_here'
export TIMEGPT_API_KEY='your_timegpt_api_key_here'
```
If using Windows, set them with:
```powershell
$env:OPENAI_API_KEY='your_openai_api_key_here'
$env:TIMEGPT_API_KEY='your_timegpt_api_key_here'
```

### **3. Run the API**
Start the FastAPI server with:
```bash
uvicorn main:app --reload
```

The API will be available at:
```
http://127.0.0.1:8000/
```
Swagger UI for testing:
```
http://127.0.0.1:8000/docs
```

---

## 🧩 Algorithm & Model Overview
### **1. Financial Data Extraction**
- The API fetches financial statements and stock price data from **Yahoo Finance**.

### **2. Stock Price Forecasting with TimeGPT**
- Uses **historical stock prices** to predict **future stock prices** (3 months ahead).
- TimeGPT is an advanced time-series model optimized for forecasting financial trends.

### **3. Textual Analysis with GPT-4o-mini**
- The model generates **structured financial insights** on:
  - **Profitability**
  - **Liquidity**
  - **Indebtedness**
  - **Stock valuation**
- The output helps **interpret raw financial numbers** into actionable insights.

---

## 📈 API Example Usage
### **Request**
```json
{
   "ticker": "INTC"
}
```

### **Response**
```json
{
  "company": "Intel Corporation",
  "financials": {
    "profitability": "### Financial Analysis of Return on Assets (ROA) for Intel Corporation\n\n**ROA Value**: -9.55%\n\n#### Interpretation of the Value\nA Return on Assets (ROA) of -9.55% indicates that Intel Corporation is generating a loss relative to its total assets. This negative value suggests that the company is not efficiently utilizing its assets to generate profits, which is a concerning sign for investors and stakeholders.\n\n#### Trend Analysis\nThe recent trend for Intel's ROA has been **decreasing**. A sustained decline in ROA can signal operational inefficiencies, increased costs, or challenges in revenue generation, which may stem from competitive pressures or market changes. This trend is particularly troubling as it suggests that the company's ability to leverage its assets effectively is worsening over time.\n\n#### Industry Comparison\nWhen compared to the semiconductor industry average, which typically ranges from 10% to 20% for established companies, Intel's ROA of -9.55% is significantly below par",
    "indebtedness": "### Financial Analysis of Intel Corporation's Debt to Equity Ratio\n\n**Debt to Equity Ratio:** 0.50\n\n#### Interpretation of the Value\nA Debt to Equity (D/E) ratio of 0.50 indicates that Intel Corporation has $0.50 of debt for every dollar of equity. This is generally considered a moderate level of leverage, suggesting that the company is using a balanced approach to financing its operations through both debt and equity.\n\n#### Assessment of the Value\n- **Good or Bad?**: A D/E ratio of 0.50 is typically seen as favorable. It implies that Intel is not overly reliant on debt, which can reduce financial risk, especially in a volatile market. A lower ratio can also indicate better financial health and stability.\n\n#### Recent Trend\n- **Trend Analysis**: Intel's D/E ratio has been relatively stable in recent years, suggesting that the company has maintained a consistent approach to its capital structure. There have been no significant spikes or drops, indicating",
    "liquidity": "### Financial Analysis of Intel Corporation's Current Ratio\n\n**Current Ratio Value:** 1.33 (rounded from 1.3268659227275277)\n\n#### Interpretation of Current Ratio\nThe current ratio is a liquidity metric that measures a company's ability to cover its short-term liabilities with its short-term assets. A current ratio above 1 indicates that the company has more current assets than current liabilities, suggesting a good short-term financial health.\n\n#### Assessment of the Value\n- **Good or Bad:** A current ratio of 1.33 is generally considered acceptable. It indicates that Intel has sufficient short-term assets to meet its short-term obligations, which is a positive sign for investors and creditors. However, it is not excessively high, which could indicate inefficiency in asset utilization.\n\n#### Recent Trend\n- **Trend Analysis:** If recent financial reports show that Intel's current ratio has been increasing over the past few quarters, this would suggest improving liquidity and financial stability. Conversely, if the trend has been",
    "stock_price_forecast (3 month)": 22.141623
  }
}
```

---

## 🔮 Future Enhancements
- **Adding macroeconomic indicators (inflation, GDP, etc.)**
- **Improving forecasting with hybrid models (LSTM + TimeGPT)**
- **Building a web dashboard for visualization**

This project is a **starting point** for automated financial analytics and forecasting, with room for expansion and further optimization. 🚀
