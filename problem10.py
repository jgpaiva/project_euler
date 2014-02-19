n = 2000000
t = [True] * (n + 1)

sum = 0
for i in xrange(2, n + 1):
    if t[i]:
        sum += i
        for mark in xrange(i, n + 1, i):
            t[mark] = False
print sum
