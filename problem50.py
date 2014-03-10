from __future__ import print_function
from itertools import islice
from itertools import takewhile
limit = int(1e6)


def calc_prime_table():
    prime_table = [True] * (limit + 1)
    prime_table[0] = False
    prime_table[1] = False
    for i, val in enumerate(prime_table):
        if val:
            for mark in xrange(2 * i, limit + 1, i):
                prime_table[mark] = False
    print("table done")
    return prime_table


def calc_primes():
    primes = [i for i, val in enumerate(prime_table) if val]
    print("primes calculated")
    return primes


def calc_max_prime_index():
    def is_sum_less_than_limit(index):
        return sum(islice(primes, index, index + 21)) < limit

    max_prime_index = max(
        takewhile(is_sum_less_than_limit, xrange(len(primes))))
    print("max_prime_index is", max_prime_index)
    return max_prime_index


prime_table = calc_prime_table()
primes = calc_primes()
max_prime_index = calc_max_prime_index()


def get_sums(index, seq=primes):
    previous = 0
    for length, num in enumerate(islice(seq, index, len(seq))):
        sum_ = previous + num
        previous = sum_
        yield (sum_, length + 1)


def is_prime(n):
    return prime_table[n]


max_num = (21, 953)
for i in xrange(max_prime_index):
    for sum_, length in get_sums(i):
        if sum_ > limit:
            break
        if length > max_num[0] and is_prime(sum_):
            max_num = (length, sum_)
print(max_num)
