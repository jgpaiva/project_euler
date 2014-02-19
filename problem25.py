def fib():
    yield 1
    a = 1
    b = 0
    while True:
        r = a + b
        yield r
        b = a
        a = r


def digits(num):
    return len(str(num))

for term, val in enumerate(fib()):
    if digits(val) == 1000:
        print (term + 1), val
        break
