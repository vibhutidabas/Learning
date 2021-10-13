import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

u = pd.read_csv('EconomiesOfScale.csv')

# sns.jointplot(x='Number of Units', y='Manufacturing Cost', data=u)
# sns.pairplot(u)   #this is better, it shows all graphs
# plt.show()

x = u[['Number of Units']]
y = u['Manufacturing Cost']
x_train = x
y_train = y

poly_reg = PolynomialFeatures(degree=6)
x_columns = poly_reg.fit_transform(x_train)         #converts simple array to a multi array with polynomial coeff.
reg = LinearRegression()
reg.fit(x_columns, y_train)

#final plotting
y_predict = reg.predict(poly_reg.fit_transform(x_train))
plt.scatter(x_train, y_train, color='gray')
plt.plot(x_train, y_predict, color='blue')
plt.xlabel('number of units')
plt.ylabel('manufacturing cost')
plt.show()