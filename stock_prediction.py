import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = yf.download("AAPL", start="2024-01-01", end="2025-09-01")

df["Prediction"] = df["Close"].shift(-30)

X = np.array(df.drop(["Prediction"], axis=1))[:-30]
y = np.array(df["Prediction"])[:-30]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


model = LinearRegression()
model.fit(X_train, y_train)

acc = model.score(X_test, y_test)
print("Model Accuracy:", acc)

X_future = np.array(df.drop(["Prediction"], axis=1))[-30:]
forecast = model.predict(X_future)

valid = df[-30:].copy()
valid["Predictions"] = forecast

plt.figure(figsize=(12,6))
plt.plot(df["Close"], label="Actual Price")
plt.plot(valid[["Predictions"]], label="Predicted Price", linestyle="dashed")
plt.legend()
plt.show()
