def digits(num):
    yield num % 10, num / 10
    yield num / 10, num % 10


# num / denom == other_digit / j
for num in xrange(10, 99):
    for common_digit, other_digit in digits(num):
        if common_digit == 0:
            continue
        for j in xrange(1, 10):
            denom = int(str(common_digit) + str(j))
            if denom > num:
                if denom * other_digit == num * j:
                    print num, "/", denom, " ", other_digit, "/", j
