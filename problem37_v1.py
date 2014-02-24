digits = range(1, 10)
limit = 9999999

prime_table = [True] * (limit + 1)
prime_table[0] = False
prime_table[1] = False

for i, value in enumerate(prime_table):
    if value:
        for mark in xrange(2 * i, limit + 1, i):
            prime_table[mark] = False
print("table done")


def decompositions(num):
    s = str(num)
    for i in xrange(1, len(s) + 1):
        yield int(s[i - 1:])


def is_prime(n):
    if n > limit:
        #print("oops, {} is too large".format(n))
        return False
    return prime_table[n]


def try_digit(d):
    if not is_prime(d):
        return set()
    retval = set()
    if all(is_prime(i) for i in decompositions(d)):
        retval.add(d)
    for i in digits:
        next_num = int(str(d) + str(i))
        other_nums = try_digit(next_num)
        retval = retval.union(other_nums)
    return retval


nums = []
for i in digits:
    nums.append(try_digit(i))
print nums
print sum(j for i in nums for j in i if j >= 10)
