import turicreate
import matplotlib.pyplot as plt

sales = turicreate.SFrame('/home/kali/ML material/home_data/home_data.sframe/m_1ce96d9d245ca490.frame_idx')
train, test = sales.random_split(.8, seed=0)
sqft_model = turicreate.linear_regression.create(train, target='price', features=['sqft_living'])          #built by sqft_living

#print(sqft_model)
#plt.plot(test['sqft_living'], test['price'], '.', test['sqft_living'], sqft_model.predict(test), '-')
#plt.show()

my_features = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'zipcode']
#turicreate.show(sales['zipcode'], sales['price'])
my_features_model = turicreate.linear_regression.create(train, target='price', features=my_features)       #built by many features

# print(sqft_model.evaluate(test))
# print(my_features_model.evaluate(test))                                             #the more the features the lesser is the error(not always the case)

#pridiction for an average house
h1 = sales[sales['id']=='5309101200']
#print(h1)
print(h1['price'])
print(sqft_model.predict(h1))
print(my_features_model.predict(h1))

#prediction for a fancy house
