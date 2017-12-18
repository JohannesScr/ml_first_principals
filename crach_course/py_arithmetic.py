import math

# Arithmetic
a = 1
b = 2
c = a + b
print('Evaluate an expression {} + {} results in {}'.format(a, b, c))

# sigma{n}{i=1}
array_of_numbers = [1, 4, 3, 8, 5]
print('Sum (sigma) an vector (array) {} results in {}'.format(array_of_numbers, sum(array_of_numbers)))

print('Count a vector (array) {} results in {}'.format(array_of_numbers ,len(array_of_numbers)))

exponent = 3
base = 2
print('Exponent {} and base {} results in {}'.format(exponent, base, base**exponent))

logarithm = 4
base = 2
print('Log base {} of {} results in {}'.format(base, logarithm, math.log(logarithm, base)))

square_root = 2
print('Square root of {} results in {}'.format(square_root, math.sqrt(square_root)))

euler_power = 2
print('Euler\'s number e to the power {} is {}'.format(euler_power, math.exp(euler_power)))

natural_log = 7.38905609893065
print('Natural log (ln) base e of {} results in {}'.format(natural_log, math.log(natural_log)))

print('PI is {}'.format(math.pi))



