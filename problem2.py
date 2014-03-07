def fib():
    a = 1
    b = 0
    yield 1
    while True:
        r = a + b
        yield r
        b = a
        a = r

f = fib()
print [next(f) for _ in xrange(11)]
limit = 4000000


def v1():
    total = 0
    for val in fib():
        if val >= limit:
            break
        elif (val % 2) == 0:
            total += val
    return total
print v1()


from itertools import ifilter, takewhile


def v2():
    def ispair(x):
        return x % 2 == 0

    def islessthanlimit(x):
        return x < limit
    return sum(ifilter(ispair, takewhile(islessthanlimit, fib())))
print v2()

import timeit
print(timeit.timeit('v1()', setup='from __main__ import v1', number=1000))
print(timeit.timeit('v2()', setup='from __main__ import v2', number=1000))
