from itertools import ifilter
limit = 1000


def v1():
    total = 0
    for i in xrange(limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


def v2():
    def aux(x):
        return x % 3 == 0 or x % 5 == 0
    return sum(ifilter(aux, xrange(limit)))


import timeit
print(timeit.timeit('v1()', setup='from __main__ import v1', number=1000))
print(timeit.timeit('v2()', setup='from __main__ import v2', number=1000))
