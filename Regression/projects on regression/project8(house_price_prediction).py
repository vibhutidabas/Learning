import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import tensorflow.keras     #will only work in 64 bit windows
from keras.models import Sequential
from keras.layers import Dense

h = pd.read_csv('kc_house_data.csv')

#visualise data by heatmap

selected_feat = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'sqft_above', 'sqft_basement']
x = h[selected_feat]
y = h['price']

#scales every value from 0 to 1
scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x)
y = y.values.reshape(-1,1)
y_scaled = scaler.fit_transform(y)

x_train, x_test, y_train, y_test = train_test_split(x_scaled, y_scaled, test_size=0.25)

model = Sequential()
model.add(Dense(50, input_dim= 7, activation = 'relu'))
model.add(Dense(50, activation = 'relu'))
model.add(Dense(100, activation = 'relu'))
model.add(Dense(1, activation = 'linear'))
model.compile(optimizer = 'Adam', loss = 'mean_squared_error')
epoch_hist = model.fit(x_train, y_train, epochs = 100, batch_size = 50, validation_split = 0.2)
