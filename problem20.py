import math
from itertools import imap


def v1():
    return sum(map(int, str(math.factorial(100))))
print v1()


def v2():
    return sum(imap(int, str(math.factorial(100))))
print v2()


def v3():
    return sum(int(i) for i in str(math.factorial(100)))
print v3()


import timeit
print(timeit.timeit('v1()', setup='from __main__ import v1', number=100000))
print(timeit.timeit('v2()', setup='from __main__ import v2', number=100000))
print(timeit.timeit('v3()', setup='from __main__ import v3', number=100000))
