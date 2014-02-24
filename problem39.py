# a + b > c
# a + c > b
# b + c > a


def istriangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


def issquare(a, b, c):
    hypo = max((a, b, c))
    others = [a, b, c]
    others.remove(hypo)
    return sum(map(lambda x: x ** 2, others)) == hypo ** 2

# c = p - a - b
# c >= a
# p - a - b >= a
# b <= p - 2a

all_triangles = list()
for p in xrange(3, 1000):
    triangles = set()
    all_triangles.append(triangles)
    for a in xrange(1, p):
        for b in xrange(1, p - 2 * a + 1):
            c = p - a - b
            if c > 0 and c >= b and a >= b \
                    and sum((a, b, c)) == p \
                    and istriangle(a, b, c) and issquare(a, b, c):
                triangles.add((a, b, c))
max_num = max(map(len, all_triangles))
print list(i + 3 for i, val in enumerate(all_triangles) if len(val) == max_num)
