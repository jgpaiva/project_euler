#!/usr/bin/env python
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

p = primes()
primes = [next(p) for _ in xrange(10001)]
print primes[-1]
