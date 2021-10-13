import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

i = pd.read_csv('IceCreamData.csv')
x = i[['Temperature']]
y = i[['Revenue']]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)

#training with an intercept
r = LinearRegression(fit_intercept = True)
r.fit(x_train, y_train)

# print('model slope(m): ' + r.coef_)
# print('model intercept(c): ' + r.intercept_)

plt.scatter(x_train, y_train, color = 'gray')
#predicting revenue from x_train and then plotting the graph
plt.plot(x_train, r.predict(x_train), color = 'red')
plt.ylabel('Revenue[Dollars]')
plt.xlabel('Temperature[degrees]')
plt.title('Revenue gen. v/s temperature--(training data)')
plt.show()

#predicting revenue from a given value
# t = [[40]]
# revenue = r.predict(t)
# print(revenue)