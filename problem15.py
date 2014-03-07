from collections import namedtuple


size = 20
Point = namedtuple('Point', ['x', 'y'])
start = Point(0, 0)
end = Point(size, size)

m = [(list(None for i in xrange(size + 1))) for i in xrange(size + 1)]


def get_m(p):
    return m[p.x][p.y]


def set_m(p, val):
    m[p.x][p.y] = val


def dfs(start):
    def update_m(nextPoint, retVal):
        val = dfs(nextPoint)
        set_m(nextPoint, val)
        retVal += val
        return retVal

    retVal = 0
    if start == end:
        return 1
    if get_m(start) is not None:
        return get_m(start)
    retVal = 0
    if start.x < size:
        nextPoint = Point(start.x + 1, start.y)
        retVal = update_m(nextPoint, retVal)
    if start.y < size:
        nextPoint = Point(start.x, start.y + 1)
        retVal = update_m(nextPoint, retVal)
    return retVal

print dfs(start)
