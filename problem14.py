max_num = 1000000


def sequencer(start):
    current = start
    yield start
    while current != 1:
        if current % 2 == 0:
            current = current // 2
        else:
            current = current * 3 + 1
        yield current


res = [None] * (2 * max_num)

max_reached = (0, 0)
for i in xrange(2, max_num + 1):
    for counter, seq in enumerate(sequencer(i)):
        if len(res) > seq and res[seq] is not None:
            counter = counter + res[seq]
            break
    res[i] = counter + 1
    if res[i] > max_reached[1]:
        max_reached = (i, res[i])
print max_reached
