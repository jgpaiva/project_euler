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
    for i in naturals(primes[-1] + 1):
        if not any(is_divisible(i, p) for p in primes):
            yield i
            primes.append(i)

number = 600851475143

factors = []
for prime in primes():
    if number == 1:
        break
    while is_divisible(number, prime):
        number /= prime
        factors.append(prime)
print factors
