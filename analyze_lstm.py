# analyze_lstm.py
# LSTM şablon (çok basit, eğitim amacıyla)
import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

df = pd.read_csv('../sample_data/finance_timeseries.csv', parse_dates=['date'])
df = df.set_index('date').asfreq('MS')
ts = df['revenue'].fillna(method='ffill').values.reshape(-1,1)

scaler = MinMaxScaler()
scaled = scaler.fit_transform(ts)

# prepare sequences
def create_seq(data, n_steps=12):
    X, y = [], []
    for i in range(len(data)-n_steps):
        X.append(data[i:i+n_steps])
        y.append(data[i+n_steps])
    return np.array(X), np.array(y)

n_steps = 12
X, y = create_seq(scaled, n_steps)
if len(X) == 0:
    print('Not enough data for LSTM sequence. Need at least', n_steps+1, 'rows.')
else:
    model = Sequential()
    model.add(LSTM(50, activation='tanh', input_shape=(n_steps, 1)))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y, epochs=10, batch_size=8, verbose=1)
    preds = model.predict(X[-6:])
    preds = scaler.inverse_transform(preds)
    print('LSTM last predictions:')
    print(preds.flatten())
    plt.figure()
    plt.plot(ts[-len(preds):], label='Actual')
    plt.plot(preds, label='Predicted')
    plt.legend()
    plt.savefig('lstm_forecast.png')
    print('Saved lstm_forecast.png')
