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
    c_num = num
    decomp = defaultdict(int)
    for i in primes():
        while is_divisible(c_num, i):
            c_num = c_num / i
            decomp[i] += 1
        if c_num == 1:
            break
    return decomp

num = 20
decomp = defaultdict(int)
for i in xrange(1, num + 1):
    for p, o in prime_decomposition(i).iteritems():
        if decomp[p] < o:
            decomp[p] = o

print(reduce(lambda x, y: x * y,
      map(lambda x: x[0] ** x[1], decomp.iteritems())))
