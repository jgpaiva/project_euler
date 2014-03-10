from itertools import izip
limit = 1000000


def ispalindrome(num):
    for i, j in zip(num, reversed(num)):
        if i != j:
            return False
    else:
        return True


def ispalindrome2(num):
    return all(i == j for i, j in izip(num, reversed(num)))


def ispalindrome3(num):
    for i, j in izip(num, reversed(num)):
        if i != j:
            return False
    else:
        return True


def v1():
    palindromes = []
    for i in xrange(limit):
        if i % 2 == 0:  # only off numbers have '1' in the end
            continue
        if ispalindrome(str(i)) and ispalindrome(bin(i)[2:]):
            palindromes.append(i)
    return sum(palindromes)
print v1()


def v2():
    palindromes = []
    for i in xrange(limit):
        if i % 2 == 0:  # only off numbers have '1' in the end
            continue
        if ispalindrome2(str(i)) and ispalindrome2(bin(i)[2:]):
            palindromes.append(i)
    return sum(palindromes)
print v2()


def v3():
    palindromes = []
    for i in xrange(limit):
        if i % 2 == 0:  # only off numbers have '1' in the end
            continue
        if ispalindrome3(str(i)) and ispalindrome3(bin(i)[2:]):
            palindromes.append(i)
    return sum(palindromes)
print v3()

import timeit
print(timeit.timeit('v1()', setup='from __main__ import v1', number=10))
print(timeit.timeit('v2()', setup='from __main__ import v2', number=10))
print(timeit.timeit('v3()', setup='from __main__ import v3', number=10))
