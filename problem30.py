power = 5
digit_powers = [i ** power for i in xrange(10)]
limit = 999999  # from here on, number is always larger than sum


def digits(num):
    digits = []
    while num >= 10:
        digits.append(num % 10)
        num = num / 10
    digits.append(num)
    return reversed(digits)

matches = []
for num in xrange(32, limit):
    if sum(digit_powers[digit] for digit in digits(num)) == num:
        matches.append(num)
print matches
print sum(matches)
