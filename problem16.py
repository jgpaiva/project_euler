def v1():
    sum = 0
    for i in str(2 ** 1000):
        sum += int(i)
    return sum
print v1()


def v2():
    return sum(int(i) for i in str(2 ** 1000))
print v2()

import timeit
print(timeit.timeit('v1()', setup='from __main__ import v1', number=100000))
print(timeit.timeit('v2()', setup='from __main__ import v2', number=100000))
