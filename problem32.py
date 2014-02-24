def are_pandigital(a, b, c):
    a, b, c = (str(x) for x in (a, b, c))
    lens = sum(len(s) for s in (a, b, c))
    numbers = set(a + b + c)
    return lens == 9 and len(numbers) == 9 and '0' not in numbers

pandigital = []
for i in xrange(1, 99):
    for j in xrange(i, 9999):
        if are_pandigital(i, j, i * j):
            pandigital.append((i, j, i * j))

print sum(set(i[2] for i in pandigital))
