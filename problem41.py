limit = 99999999

prime_table = [True] * (limit + 1)
prime_table[0] = False
prime_table[1] = False

sets = [set(str(j) for j in xrange(1, i + 1)) for i in xrange(1, 10)]


def is_pandigital(n):
    n = str(n)
    len_a = len(n)
    numbers = set(n)
    return len_a == len(numbers) and numbers == sets[len_a - 1]

for i in xrange(limit + 1):
    if prime_table[i]:
        for mark in xrange(2 * i, limit + 1, i):
            prime_table[mark] = False
print("table done")

pandigitals = []
for i in xrange(2143, limit):
    if prime_table[i] and is_pandigital(i):
        pandigitals.append(i)
print pandigitals[-1]
