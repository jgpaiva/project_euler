coins = [1, 2, 5, 10, 20, 50, 100, 200]

# 1 = {1}
# 2 = {(1,1),(2)}
# 3 = {(1,1,1),(1,2)}
# 4 = {(1,1,1,1),(1,1,2),(2,2)}
# 5 = {(1,1,1,1,1),(1,1,1,2),(1,2,2),(5)}

combinations = {}
for value in xrange(1, 201):
    combinations[value] = set()
    for coin in coins:
        if coin == value:
            combinations[value].add((coin,))
        elif coin < value:
            for i in combinations[value - coin]:
                combinations[value].add(tuple(sorted(i + (coin,))))
print combinations[5]
print len(combinations[200])
