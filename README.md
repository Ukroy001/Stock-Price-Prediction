# Stock-Price-Prediction
# 📈 Stock Price Prediction with Linear Regression  

This project demonstrates a **basic machine learning approach** to predict stock prices using historical data from **Yahoo Finance**. It applies **linear regression** on Apple (AAPL) stock data to forecast the next 30 days of closing prices.  

---

## 🚀 Features  
- Fetches real stock data using [yfinance](https://pypi.org/project/yfinance/).  
- Prepares training and testing datasets with a **30-day prediction window**.  
- Implements a **Linear Regression** model using scikit-learn.  
- Visualizes **actual vs. predicted** stock prices.  

---

## 📂 Project Structure  
```bash
├── stock_prediction.py # Main code file
├── README.md # Documentation
```
---

## ⚙️ Installation & Setup  

1. Clone the repo:
   ```bash
   git clone https://github.com/Ukroy001/Stock-Price-Prediction.git
   cd stock-price-prediction
   ```
2. Install dependencies:
```bash
  pip install yfinance pandas numpy matplotlib scikit-learn
```
3. Run the script:
   ```bash
   python stock_prediction.py
---

## 📊 Example Output:

      -Model Accuracy is displayed in the terminal.
      -A chart will pop up showing actual vs. predicted stock prices:

  ---

  ## ⚠️ Limitations:
  ```
      1.Linear Regression is too simple: Stock prices are influenced by complex factors (news, market sentiment, global events) not captured here.
    
      2.Overfitting risk: The model only learns from historical data and may not generalize well.
      
      3.No external features: Uses only historical closing prices, ignoring trading volume, financial reports, or macroeconomic indicators.
      
      4.Short prediction horizon: Works only for 30-day ahead forecasting, but you can extend the training data window for potentially better accuracy.
      
      5.Not financial advice: This project is for educational purposes only and should not be used for real trading decisions.
