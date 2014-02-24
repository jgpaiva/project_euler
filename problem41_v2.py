from itertools import permutations
from math import ceil

limit = int(ceil(7654321 ** 0.5))

prime_table = [True] * (limit + 1)
prime_table[0] = False
prime_table[1] = False


for i, val in enumerate(prime_table):
    if val:
        for mark in xrange(2 * i, limit + 1, i):
            prime_table[mark] = False
print("table done")
primes = [i for i, val in enumerate(prime_table) if val]


largest = 2143
for n in xrange(1, 8):  # all pandigitals with 8 or 9 are divisible by 3
    for perm in permutations(xrange(1, n + 1)):
        num = sum(n * 10 ** i for i, n in enumerate(reversed(perm)))
        if not any(num % i == 0 for i in primes) and num > largest:
            largest = num
print largest
