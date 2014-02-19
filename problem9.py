def get_square(squares, index):
    if squares[index] == 0:
        squares[index] = index ** 2
    return squares[index]

n = 1000
up_to = 1000

squares = [0] * 1000

for i in xrange(1, up_to):
    for j in xrange(i + 1, up_to):
        for k in xrange(j + 1, up_to):
            if i + j + k != 1000:
                continue

            if(get_square(squares, i) + get_square(squares, j) ==
               get_square(squares, k)):
                print i, j, k
