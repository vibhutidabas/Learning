import turicreate
import math
import random
import numpy
import matplotlib.pyplot as plt

random.seed(98103)
n = 30
x = turicreate.SArray([random.random() for i in range(n)]).sort()

# compute y
y = x.apply(lambda x: math.sin(4*x))

# add random gaussian noise e to y
random.seed(1)
e = turicreate.SArray([random.gauss(0, 1.0/3.0) for j in range(n)])
y += e

# put data into an SFrame to manipulate later
data = turicreate.SFrame({'X1': x, 'Y': y})
print(data)

# create a func to plot the data
def plot_data(data):
    plt.plot(data['X1'], data['Y'], 'k.')
    plt.xlabel('x')
    plt.ylabel('y')

# plot_data(data)
# plt.show()

# a func to create our features for poly reg.
def poly_feat(data, deg):
    data_copy = data.copy()
    for i in range(1, deg):
        data_copy['X'+str(i+1)] = data_copy['X'+str(i)]*data_copy['X1']
    return data_copy

def plot_poly(data, model):
    plot_data(data)
    deg = len(model.coefficients['value'])-1
    x_pred = turicreate.SFrame({'X1': [i/200.0 for i in range(200)]})
    y_pred = model.predict(poly_feat(x_pred, deg))
    plt.plot(x_pred['X1'], y_pred, 'g-', label='degree' + str(deg) + 'fit')
    plt.legend(loc='upper left')
    plt.axis([0, 1, -1.5, 2])
    plt.show()

def print_coeff(model):
    deg = len(model.coefficients['value'])-1
    w = list(model.coefficients['value'])
    print('learned poly degrees'+str(deg)+':')
    w.reverse()
    print(numpy.poly1d(w))

def poly_lasso(data, deg, l1_penalty):
    model = turicreate.linear_regression.create(poly_feat(data, deg), target='Y', l2_penalty=0., l1_penalty=l1_penalty, validation_set=None,
                                                solver='fista', verbose=False, max_iterations=3000, convergence_threshold=1e-10)
    return model

for l1_penalty in [0.0001, 0.01, 0.1, 10]:
    model = poly_lasso(data, deg=16, l1_penalty=l1_penalty)
    print('l1_penalty = %e' % l1_penalty)
    print('number of non zeros = %d' % (model.coefficients['value']).nnz())
    print_coeff(model)
    print('\n')
    plt.figure()
    plot_poly(data, model)
    plt.title('LASSO, lambda = %.2e, # nonzeros = %d' % (l1_penalty, (model.coefficients['value']).nnz()))






