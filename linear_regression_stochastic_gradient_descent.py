# MACHINE LEARNING FROM FIRST PRINCIPALS

"""
LINEAR REGRESSION

Based on theory and first principals, the aim is to build simple linear
regression model, to understand how linear regression works and how
one would go about implementing it, should there ever be a need to that
a library does not support.

Linear regression is a model that assumes a linear relationship between
the input variable (x) and the single output (y). When there is a single
input variable (x) the method is referred to as simple linear regression.

When there are multiple input variables (x), literature from statistics
refers to the method as multiple linear regression.

"""
import math

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 3, 2, 3, 5])

# initiate variables
B0 = 0
B1 = 0
alpha = 0.1
iterations = np.arange(0, 41)
i = 0
error = []

# gradient descent for 40 iterations
for _ in iterations:
    # make prediction
    p_ = B1 * x[i] + B0
    # calculate error
    delta = p_ - y[i]
    error.append(delta)
    # update weights
    B0 = B0 - alpha * delta  # still to derive how to get this function
    B1 = B1 - alpha * delta * x[i]  # still to derive how to get this function
    # increment counter to go through epochs
    i += 1
    if i == 4:  # reset counter
        i = 0
    print(i, delta, B0, B1)

# make final predictions
p_ = B1 * x + B0

# plot the error graph
plt.plot(iterations, error)
plt.show()

# plot the output(y) and prediction(p_) against input (x)
plt.plot(x, y)
plt.plot(x, p_)
plt.show()

# RMSE
RMSE = math.sqrt(sum((p_ - y) ** 2) / len(p_))
