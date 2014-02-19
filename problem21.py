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

max_num = 10000
cache = [None] * max_num


def cacheddivisors(num):
    if cache[num] is None:
        cache[num] = divisors(num)
    return cache[num]


numbers = []
for i in xrange(1, max_num):
    div, div_sum = cacheddivisors(i)
    if div_sum < max_num and div_sum != i:
        if cacheddivisors(div_sum)[1] == i:
            numbers.append(i)

print numbers, sum(numbers)
