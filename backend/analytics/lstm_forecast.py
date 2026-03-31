import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

def train_lstm(df):
    scaler = MinMaxScaler()
    data = scaler.fit_transform(df)

    X, y = [], []
    for i in range(len(data)-3):
        X.append(data[i:i+3])
        y.append(data[i+3][0])

    X, y = np.array(X), np.array(y)

    model = Sequential([
        LSTM(32, input_shape=(X.shape[1], X.shape[2])),
        Dense(1)
    ])
    model.compile(optimizer="adam", loss="mse")
    model.fit(X, y, epochs=20, verbose=0)

    return model, scaler
