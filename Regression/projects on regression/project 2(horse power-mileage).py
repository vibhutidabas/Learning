import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

f = pd.read_csv('FuelEconomy.csv')
x = f[['Horse Power']]
y = f[['Fuel Economy (MPG)']]

#division of data in train and test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)

#training with an intercept!=0
r = LinearRegression(fit_intercept = True)
r.fit(x_train, y_train)

# print('model slope(m): ' + r.coef_)
# print('model intercept(c): ' + r.intercept_)

plt.scatter(x_train, y_train, color = 'gray')
#predicting revenue from x_train and then plotting the graph(the red line)
plt.plot(x_train, r.predict(x_train), color = 'red')
#side line labels
plt.ylabel('Fuel Economy[dollars]')
plt.xlabel('Horse Power')
plt.title('economy v/s power--(training data)')
plt.show()

#predicting mileage from a given value
# hp = [[15.5]]
# fe = r.predict(hp)
# print(fe)