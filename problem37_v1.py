digits = [1, 3, 7, 9]
limit = 99999999

prime_table = [True] * (limit + 1)
prime_table[0] = False
prime_table[1] = False

for i in xrange(limit + 1):
    if prime_table[i]:
        for mark in xrange(2 * i, limit + 1, i):
            prime_table[mark] = False
print("table done")


def decompositions(num):
    s = str(num)
    for i in xrange(1, len(s) + 1):
        yield int(s[i - 1:])


def is_prime(n):
    if n > limit:
        raise Exception("oops, {} is too large".format(n))
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
    print(retval)
    return retval


nums = []
for i in digits:
    nums.append(try_digit(i))
print nums
