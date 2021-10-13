import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from math import sqrt
from mpl_toolkits.mplot3d import Axes3D

a = pd.read_csv('Admission.csv')

# sns.pairplot(a)
# plt.show()
# print(a.info())                    # gives all the info about a

a = a.drop(['Serial No.'], axis = 1)
#shows the correalation between two things
# plt.figure(figsize = (10,10))
# sns.heatmap(a.corr(), annot = True)
# plt.show()

x = a[['GRE Score', 'TOEFL Score']]
y = a['Admission Chance']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

reg = LinearRegression(fit_intercept=True)
reg.fit(x_train, y_train)
y_predict = reg.predict(x_test)

#error were computed in project 5
# k = x_test.shape[1]
# n = len(x_test)
# RMSE = float(format(np.sqrt(mean_squared_error(y_test, y_predict)), '.3f'))
# MSE = mean_squared_error(y_test, y_predict)
# MAE = mean_absolute_error(y_test, y_predict)
# r2 = r2_score(y_test, y_predict)
# adj_r2 = 1-(1-r2) * (n-1)/(n-k-1)
# MAPE = np.mean(np.abs(y_test-y_predict)/(y_test))*100

#eg: x_surf is a matrix of 100X100
x_surf, y_surf = np.meshgrid(np.linspace(a['GRE Score'].min(), a['GRE Score'].max(), 100), np.linspace(a['TOEFL Score'].min(), a['TOEFL Score'].max(), 100))
#to flatten the matrix we ravel
onlyx = pd.DataFrame({'GRE Score': x_surf.ravel(), 'TOEFL Score': y_surf.ravel()})
#now it's 10000X2

fittedy = reg.predict(onlyx)
fittedy = fittedy.reshape(x_surf.shape)

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(a['GRE Score'], a['TOEFL Score'], a['Admission Chance'], c='black', marker='o')
ax.plot_surface(x_surf, y_surf, fittedy, color='red', alpha=0.3)
ax.set_xlabel('GRE Score')
ax.set_ylabel('TOEFL Score')
ax.set_zlabel('Admission Chance')
plt.show()