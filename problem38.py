sets = [set(str(j) for j in xrange(1, i + 1)) for i in xrange(1, 10)]


def is_pandigital_str(n):
    len_a = len(n)
    numbers = set(n)
    return len_a == len(numbers) and numbers == sets[len_a - 1]


def numbers():
    yield 9
    for i in xrange(91, 100):
        yield i
    for i in xrange(918, 1000):
        yield i
    for i in xrange(9182, 10000):
        yield i


def main():
    largest = 918273645
    for n in xrange(2, 9):
        for i in numbers():
            num_str = "".join(str(i * j) for j in xrange(1, n + 1))
            if len(num_str) > 9:
                break
            num = int(num_str)
            if num > largest and is_pandigital_str(num_str):
                largest = num
                print largest
    print largest

main()
