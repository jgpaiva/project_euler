max_ceiling = 28123


def divisors(num):
    retval = [1]
    limit = num / 1
    for i in xrange(2, num):
        if i >= limit:
            break
        if num % i == 0:
            limit = num / i
            retval.append(i)
            if num / i > i:
                retval.append(num / i)
    return retval, sum(retval)


whatis = [None] * (max_ceiling + 1)
for i in xrange(1, max_ceiling + 1):
    div, div_sum = divisors(i)
    if div_sum == i:
        whatis[i] = 0
    elif div_sum > i:
        whatis[i] = 1
    else:
        whatis[i] = -1


def isabundant(n):
    return whatis[n] is not None and whatis[n] > 0

can = [False] * (max_ceiling + 1)
for i in xrange(1, max_ceiling + 1):
    if isabundant(i):
        for j in xrange(i, max_ceiling + 1):
            if isabundant(j) and i + j <= max_ceiling:
                can[i + j] = True

s = 0
for i in xrange(1, max_ceiling + 1):
    if not can[i]:
        s += i
print s
