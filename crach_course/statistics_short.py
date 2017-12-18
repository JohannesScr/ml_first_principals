import random
import statistics
from scipy.stats import pearsonr
from scipy.stats import invgauss
from scipy.stats import norm

vector = [1, 23, 4, 13, 9, 7, 7, 13, 4, 23, 1, 23, 1, 23, 3, 23]

print('Vector {}'.format(vector))
print('Average of the vector is {}'.format(statistics.mean(vector)))

print('Mode of the vector is {}'.format(statistics.mode(vector)))

print('Median of the vector is {}'.format(statistics.median(vector)))

print('Standard deviation (sigma) of the vector is {}'.format(statistics.stdev(vector)))

vector_one = [1, 2, 3]
vector_two = [4, 5, 6]
vector_three = [9, 8, 7]

print('Positive correlation with pearson between {} and {} is {}'.format(vector_one, vector_two,
                                                                         pearsonr(vector_one, vector_two)))
print('Negative correlation with pearson between {} and {} is {}'.format(vector_one, vector_three,
                                                                         pearsonr(vector_one, vector_three)))

print('Random number {}'.format(random.random()))
invgauss_mu = 10
invgauss_loc = 10
print('Gaussian random number {}'.format(invgauss.rvs(invgauss_mu, invgauss_loc)))
norm_loc = 10
print('Normal distribution random variates {}'.format(norm.rvs(norm_loc)))
