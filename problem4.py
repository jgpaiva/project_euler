#!/usr/bin/env python


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

print parts(10019012)
print is_palindrome(10019012)
print is_palindrome(10001)
print is_palindrome(1001)

max_pal = 0
max_num = 1000
for i in range(1, max_num):
    for j in range(i, max_num):
        if is_palindrome(i * j) and i * j > max_pal:
            max_pal = i * j
print max_pal
