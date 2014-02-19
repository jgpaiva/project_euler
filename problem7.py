#!/usr/bin/env python


def is_divisible(a, b):
    return a % b == 0


def naturals(start=0):
    count = start
    while True:
        count += 1
        yield count


def primes():
    primes = [2, 3, 5, 7]
    for i in primes:
        yield i
    for i in naturals(primes[-1]):
        for p in primes:
            if is_divisible(i, p):
                break
        else:
            yield i
            primes.append(i)

p = primes()
primes = [next(p) for _ in xrange(10001)]
print primes[-1]
