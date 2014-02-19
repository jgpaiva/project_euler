def fib():
    a = 1
    b = 0
    yield 1
    while True:
        r = a + b
        yield r
        b = a
        a = r

f = fib()
print [next(f) for _ in xrange(11)]

total = 0
for val in fib():
    if val >= 4000000:
        break
    elif (val % 2) == 0:
        total += val
print total
