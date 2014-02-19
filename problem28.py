def naturals():
    counter = 1
    while True:
        yield counter
        counter += 1


def gen_spiral():
    c = naturals()
    yield next(c)
    space = 1
    while True:
        for i in xrange(4):
            for i in xrange(space):
                next(c)
            yield next(c)
        space += 2

g = gen_spiral()
l = []
for i in xrange(2001):
    l.append(next(g))
print l
print sum(l)
