def sum_of_squares(num):
    return sum(i ** 2 for i in xrange(num + 1))


def square_of_sums(num):
    return sum(xrange(num + 1)) ** 2

n = 100
print square_of_sums(n) - sum_of_squares(n)
