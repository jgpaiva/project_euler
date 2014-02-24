from itertools import count


def digit_set(n):
    return tuple(sorted(str(n)))

for x in count(2):
    if len(str(x)) == len(str(6 * x)):
        d_set = digit_set(x)
        if all(d_set == digit_set(x * num) for num in xrange(2, 7)):
            print map(lambda y: x * y, xrange(1, 7))
            break
