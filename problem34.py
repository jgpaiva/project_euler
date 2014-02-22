from math import factorial
from itertools import count


digit_factorials = [factorial(digit) for digit in xrange(10)]


for i in count(1):
    if i * digit_factorials[9] < int('9' * i):
        print i
        break
# 7


def digits(num):
    digits = []
    while num >= 10:
        digits.append(num % 10)
        num = num / 10
    digits.append(num)
    return reversed(digits)

matches = []
for num in xrange(3, int('9' * 7)):
    if sum(digit_factorials[digit] for digit in digits(num)) == num:
        matches.append(num)
print matches
print sum(matches)
