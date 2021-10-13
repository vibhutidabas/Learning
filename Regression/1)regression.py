import turicreate
import matplotlib.pyplot as plt

sales = turicreate.SFrame('/home/kali/ML material/philadelphia crime rate/Philadelphia_Crime_Rate_noNA.csv')

# plt.plot(sales['CrimeRate'], sales['HousePrice'], '.')
# plt.show()

# using crime as a feature
crime_model = turicreate.linear_regression.create(sales, target='HousePrice', features=['CrimeRate'], validation_set=None, verbose=False)
# plt.plot(sales['CrimeRate'], sales['HousePrice'], '.', sales['CrimeRate'], crime_model.predict(sales), '-')
# plt.show()

# removing centre city
sales_noCC = sales[sales['MilesPhila'] != 0]
crime_model_noCC = turicreate.linear_regression.create(sales_noCC, target='HousePrice', features=['CrimeRate'], validation_set=None, verbose=False)
# plt.plot(sales_noCC['CrimeRate'], sales_noCC['HousePrice'], '.', sales_noCC['CrimeRate'], crime_model_noCC.predict(sales_noCC), '-')
# plt.show()

# comparision of prices after removing central city
# print(crime_model.coefficients)
# print(crime_model_noCC.coefficients)

# after removing high ends (not much difference)
sales_nohighend = sales_noCC[sales_noCC['HousePrice'] < 350000]
crime_model_nohighend = turicreate.linear_regression.create(sales_nohighend, target='HousePrice', features=['CrimeRate'], validation_set=None, verbose=False)
# plt.plot(sales_nohighend['CrimeRate'], sales_nohighend['HousePrice'], '.', sales_nohighend['CrimeRate'], crime_model_nohighend.predict(sales_nohighend), '-')
# plt.show()


















