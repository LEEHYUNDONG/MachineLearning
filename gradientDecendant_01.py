def sum_of_squares(v):
    return sum(v_i ** 2 for v_i in v)


def difference_quotient(f, x, h):
    return (f(x + h) - f(x)) / h


def square(x):
    return x**2


def derivative(x):
    return 2 * x


derivative_estimate = lambda x: difference_quotient(square, x, h = 0.00001)

import matplotlib.pyplot as plt
x = range(-10, 10)

plt.title("Actual Derivatives vs. Estimates")
plt.plot(x, map(derivative, x), 'rx', label = 'Actual')
plt.plot(x, map(derivative_estimate, x), 'b+', label = 'Estimate')
plt.legend(loc=9)
plt.show()
