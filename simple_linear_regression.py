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

import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.stats import pearsonr
import statistics as stats

# input variable
x = np.array([1, 2, 4, 3, 5])

# output variable
y = np.array([1, 3, 3, 2, 5])

plt.scatter(x, y)
# plt.show()

# we want to model our data as follows
# y = (B1 * x) + B0
# y is the output variable (we want to predict / dependent variable)
# B0 (bias) and B1 (slope) are the coefficients we want to calculate
# x is the input variables (independent variable)

# Estimating B1
# B1 = sum(x_i - mean(x)) * sum(y_i - mean(y)) / sum( (x_i - mean(x)) ** 2 )

# Estimating B0
# B0 = mean(y) - B1 * mean(x)

mean_x = sum(x)/len(x)
mean_y = sum(y)/len(y)

x_minus_mean_x = x - mean_x

x_minus_mean_x_squared = x_minus_mean_x ** 2

y_minus_mean_y = y - mean_y

x_minus_mean_x_times_y_minus_mean_y = x_minus_mean_x * y_minus_mean_y

# calculate B1
B1 = sum(x_minus_mean_x_times_y_minus_mean_y) / sum(x_minus_mean_x_squared)

# calculate B0
B0 = mean_y - B1 * mean_x

# make predictions
p_ = B1 * x + B0

plt.plot(x, p_)
plt.show()

# estimating error
# Root Mean Squared Error
# RMSE = sqrt(sum((p_i - y_i) ** 2)/ len(p))

RMSE = math.sqrt(sum((p_ - y) ** 2) / len(p_))
# RMSE = 0.69
# Therefore we are on average wrong by about 0.48 units

# Alternative to calculate B1
# B1 = correlation(x, y) * standard_deviation(y) / standard_deviation(x)
B1_alternative = pearsonr(x, y)[0] * stats.stdev(y, mean_y) / stats.stdev(x, mean_x)










