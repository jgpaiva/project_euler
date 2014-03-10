from itertools import permutations
from itertools import islice

primes = [2, 3, 5, 7, 11, 13, 17]


def is_divisible(div, permutation, start):
    n = sum(i * exp for exp,
            i in zip([100, 10, 1], islice(permutation, start, start + 3)))
    return n % div == 0

retval = []
for permutation in permutations(xrange(10)):
    for div, start in zip(primes, xrange(1, 8)):
        if not is_divisible(div, permutation, start):
            break
    else:
        retval.append(permutation)
print retval
print sum(int(''.join(str(i) for i in perm)) for perm in retval)

#can be optimized by avoiding dividing for already tested situations
