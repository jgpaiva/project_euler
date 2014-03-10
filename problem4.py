from itertools import izip
limit = 1000


def parts(num):
    c_num = num
    parts = []
    while c_num >= 10:
        parts.append(c_num % 10)
        c_num /= 10
    parts.append(c_num)
    return parts


def is_palindrome(num):
    num = parts(num)
    return all(map(lambda x: x[0] == x[1], zip(num, reversed(num))))


def is_palindrome2(num):
    num = parts(num)
    return all(a == b for a, b in izip(num, reversed(num)))


def v1():
    max_pal = 0
    for i in range(1, limit):
        for j in range(i, limit):
            if is_palindrome(i * j) and i * j > max_pal:
                max_pal = i * j
    return max_pal
print v1()


def v2():
    max_pal = 0
    for i in range(1, limit):
        for j in range(max(i, max_pal / i), limit):
            mul = i * j
            if mul > max_pal and is_palindrome2(mul):
                max_pal = mul
    return max_pal
print v2()

import timeit
print(timeit.timeit('v1()', setup='from __main__ import v1', number=10))
print(timeit.timeit('v2()', setup='from __main__ import v2', number=10))
