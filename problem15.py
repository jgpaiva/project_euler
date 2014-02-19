from collections import namedtuple


size = 20
Point = namedtuple('Point', ['x', 'y'])
start = Point(0, 0)
end = Point(size, size)

m = [(list(None for i in xrange(size + 1))) for i in xrange(size + 1)]


def dfs(start):
    retVal = 0
    if start == end:
        return 1
    if m[start.x][start.y] is not None:
        return m[start.x][start.y]
    retVal = 0
    if start.x < size:
        nextPoint = Point(start.x + 1, start.y)
        val = dfs(nextPoint)
        m[nextPoint.x][nextPoint.y] = val
        retVal += val
    if start.y < size:
        nextPoint = Point(start.x, start.y + 1)
        val = dfs(nextPoint)
        m[nextPoint.x][nextPoint.y] = val
        retVal += val
    return retVal

print dfs(start)
