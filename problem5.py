#!/usr/bin/env python
from collections import defaultdict


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


def primes_smaller_than(num):
    retval = []
    for i in primes():
        if i >= num:
            break
        retval.append(i)
    return retval


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

print(prime_decomposition(24))

num = 20
decomp = defaultdict(int)
for i in xrange(1, num + 1):
    for p, o in prime_decomposition(i).iteritems():
        if decomp[p] < o:
            decomp[p] = o

print(reduce(lambda x, y: x * y,
      map(lambda x: x[0] ** x[1], decomp.iteritems())))


#n = 10
#factors = []
#num = 1
#for i in xrange(n, 0, -1):
#    if is_divisible(num, i):
#        pass
#    else:
#        factors.append(i)
#        num *= i
#
#print factors
#print num

#print(reduce(lambda x, y: x * y, primes_smaller_than(10)))
