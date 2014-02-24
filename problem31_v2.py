coins = [1, 2, 5, 10, 20, 50, 100, 200]


def memoized(funct):
    cache = {}

    def memoizer(*args):
        if args not in cache:
            cache[args] = funct(*args)
        return cache[args]
    return memoizer


@memoized
def combinations(max_coin, value):
    if max_coin == 0 or value == 0:
        return 1
    if coins[max_coin] > value:
        return combinations(max_coin - 1, value)
    return combinations(max_coin, value - coins[max_coin]) \
        + combinations(max_coin - 1, value)

print combinations(len(coins) - 1, 1000)
