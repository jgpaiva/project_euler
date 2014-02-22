from math import floor


def triangle(n):
    return n * (n + 1) / 2


def pentagonal(n):
    return n * (3 * n - 1) / 2


def hexagonal(n):
    return n * (2 * n - 1)


a = 285
b = 165
c = 144

a_val = triangle(a)
b_val = pentagonal(b)
c_val = hexagonal(c)


def find_value(lower, target, funct):
    def find_value_aux(lower, upper, target, funct):
        current = lower + floor((upper - lower) / 2)
        val = funct(current)
        if current == lower:
            return current, val
        if val == target:
            return current, val
        if val > target:
            return find_value_aux(lower, current, target, funct)
        return find_value_aux(current, upper, target, funct)

    upper = lower
    while funct(upper) < target:
        upper *= 2
    return find_value_aux(lower, upper, target, funct)


while True:
    b, b_val = find_value(b, c_val, pentagonal)
    if b_val == c_val:
        a, a_val = find_value(a, c_val, triangle)
        if a_val == c_val:
            break
    c += 1
    c_val = hexagonal(c)

print a, b, c, a_val, b_val, c_val
