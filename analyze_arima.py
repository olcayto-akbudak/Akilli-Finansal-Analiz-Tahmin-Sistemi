# analyze_arima.py
# Örnek ARIMA tahmin scripti (basit şablon)
import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

df = pd.read_csv('../sample_data/finance_timeseries.csv', parse_dates=['date'])
df = df.set_index('date').asfreq('MS')
ts = df['revenue'].fillna(method='ffill')

model = ARIMA(ts, order=(1,1,1))
model_fit = model.fit()
forecast = model_fit.get_forecast(steps=6)
pred = forecast.predicted_mean

print("Next 6 months forecast:")
print(pred)

plt.figure()
ts.plot(label='Historical')
pred.plot(label='Forecast')
plt.legend()
plt.title('ARIMA Forecast')
plt.savefig('arima_forecast.png')
print('Saved arima_forecast.png')
