limit = 1000000

is_prime = [True] * (limit + 1)
is_prime[0] = False
is_prime[1] = False


def rotations(num):
    s = str(num)
    for _ in range(len(s) - 1):
        s = rotate(s)
        yield int(s)


def rotate(s):
    return s[-1] + s[:-1]


for i in range(limit + 1):
    if is_prime[i]:
        for mark in xrange(2 * i, limit + 1, i):
            is_prime[mark] = False


circulars = []
for index, prime in enumerate(is_prime):
    if prime:
        if index < 10:
            circulars.append(index)
            continue

        r = rotations(index)
        if all(is_prime[i] for i in r):
            circulars.append(index)
            circulars.extend(r)
        for i in r:
            is_prime[i] = False
print circulars
print len(circulars)
