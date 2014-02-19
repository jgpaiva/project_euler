cache = {}


def divisors2(num):
    counter = 0
    for i in xrange(num, 0, -1):
        if num % i == 0:
            if i in cache:
                counter += cache[i]
                if i > num / i and i % (num / i) != 0:
                    counter += 1
                break
            else:
                counter += 1
    cache[num] = counter
    return counter


def divisors(num):
    counter = 2  # himself and 1
    limit = num / 1
    for i in xrange(2, num):
        if i >= limit:
            break
        if num % i == 0:
            limit = num / i
            counter += 1
            if num / i > i:
                counter += 1
    return counter

triangle = 0
for i in xrange(1, 1000000):
    triangle += i
    factors = divisors(triangle)
    if factors > 500:
        print i, triangle, factors
