#!/usr/bin/env python
from collections import defaultdict
from itertools import count


def is_divisible(a, b):
    return a % b == 0


def primes():
    primes = [2, 3, 5, 7]
    for i in primes:
        yield i
    for i in count(primes[-1] + 1):
        if not any(is_divisible(i, p) for p in primes):
            yield i
            primes.append(i)


def prime_decomposition(num):
    decomp = defaultdict(int)
    for i in primes():
        while is_divisible(num, i):
            num = num / i
            decomp[i] += 1
        if num == 1:
            break
    return decomp

num = 20
decomp = defaultdict(int)
for i in xrange(1, num + 1):
    for p, o in prime_decomposition(i).iteritems():
        if decomp[p] < o:
            decomp[p] = o


def v1():
    return reduce(lambda x, y: x * y,
                  map(lambda x: x[0] ** x[1], decomp.iteritems()))
print(v1())


from operator import mul
from itertools import starmap


def v2():
    return reduce(mul, starmap(pow, decomp.iteritems()))
print(v2())

import timeit
print(timeit.timeit('v1()', setup='from __main__ import v1', number=100000))
print(timeit.timeit('v2()', setup='from __main__ import v2', number=100000))
