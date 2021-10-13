import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from math import sqrt
from mpl_toolkits.mplot3d import Axes3D

stock = pd.read_csv('S&P500_Stock_Data.csv')

# sns.jointplot(x='Employment', y='S&P 500 Price', data=stock)
# sns.pairplot(stock)
# plt.show()

x = stock[['Interest Rates', 'Employment']]
y = stock['S&P 500 Price']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

reg = LinearRegression(fit_intercept=True)
reg.fit(x_train, y_train)
y_predict = reg.predict(x_test)

#computing all the types of error
k = x_test.shape[1]
n = len(x_test)
RMSE = float(format(np.sqrt(mean_squared_error(y_test, y_predict)), '.3f'))
MSE = mean_squared_error(y_test, y_predict)
MAE = mean_absolute_error(y_test, y_predict)
r2 = r2_score(y_test, y_predict)
adj_r2 = 1-(1-r2) * (n-1)/(n-k-1)
MAPE = np.mean(np.abs(y_test-y_predict)/(y_test))*100

#x_surf is a matrix of 100X100
x_surf, y_surf = np.meshgrid(np.linspace(stock['Interest Rates'].min(), stock['Interest Rates'].max(), 100), np.linspace(stock['Employment'].min(), stock['Employment'].max(), 100))
#to flatten the matrix we ravel
onlyx = pd.DataFrame({'Interest Rates': x_surf.ravel(), 'Employment': y_surf.ravel()})
#now it's 10000X2

fittedy = reg.predict(onlyx)
fittedy = fittedy.reshape(x_surf.shape)

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(stock['Interest Rates'], stock['Employment'], stock['S&P 500 Price'], c='black', marker='x')
ax.plot_surface(x_surf, y_surf, fittedy, color='red', alpha=0.3)
ax.set_xlabel('interest rates')
ax.set_ylabel('unemployment rates')
ax.set_zlabel('stock index price')
plt.show()