import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

s = pd.read_csv('Employee_Salary.csv')

# sns.jointplot(x='Years of Experience', y='Salary', data=s)
# sns.pairplot(s)   #this is better, it shows all graphs
# plt.show()
x = s[['Years of Experience']]
y = s['Salary']
x_train = x
y_train = y

poly_reg = PolynomialFeatures(degree=3)
x_columns = poly_reg.fit_transform(x_train)         #converts simple array to a multi array with polynomial coeff.
reg = LinearRegression()
reg.fit(x_columns, y_train)

#final plotting
y_predict = reg.predict(poly_reg.fit_transform(x_train))
plt.scatter(x_train, y_train, color='gray')
plt.plot(x_train, y_predict, color='blue')
plt.xlabel('years of experience')
plt.ylabel('salary')
plt.show()