from itertools import count

# this was fun, but it doesn't work


digits = [1, 3, 7, 9]
primes_cache = [2, 3, 5, 7]
primes_set = set(primes_cache)


def decompositions(num):
    s = str(num)
    for i in range(1, len(s) + 1):
        yield int(s[:i])


def is_divisible(a, b):
    return a % b == 0


def primes():
    for i in primes_cache:
        primes_set.add(i)
        yield i
    for i in count(primes_cache[-1] + 1):
        if not any(is_divisible(i, p) for p in primes_cache):
            primes_set.add(i)
            primes_cache.append(i)
            yield i


def is_prime(n):
    if n < primes_cache[-1]:
        return n in primes_set
    for i in primes():
        if i == n:
            return True
        if is_divisible(n, i):
            return False


def try_digit(d):
    if not is_prime(d):
        return set()
    retval = set()
    if all(is_prime(i) for i in decompositions(d)):
        retval.add(d)
    for i in digits:
        next_num = int(str(i) + str(d))
        other_nums = try_digit(next_num)
        retval = retval.union(other_nums)
    return retval


nums = []
for i in digits:
    nums.append(try_digit(i))
print nums
