input_str = """ 75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

input_str2 = """3
7 4
2 4 6
8 5 9 3"""


class Node:

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
        self.max_sum = None

    def __str__(self):
        return "[ {}, l:{},\n r:{} ]".format(self.value, self.left, self.right)

    def __repr__(self):
        return "[ {} ]".format(self.value)


count = sum(1 for line in input_str.split("\n") for _ in line.split())
tree = [None] * count
last = -1

for level, line in enumerate(input_str.split("\n")):
    for inlevel, number in enumerate(line.split()):
        pos = sum(xrange(level + 1)) + inlevel
        new_node = Node(int(number), None, None)
        tree[pos] = new_node
        if pos == 0:
            continue
        else:
            if inlevel > 0:
                left_parent = tree[sum(xrange(level)) + inlevel - 1]
                left_parent.right = new_node
            if inlevel < level:
                right_parent = tree[sum(xrange(level)) + inlevel]
                right_parent.left = new_node


def dfs(start):
    if start.left is None:
        return start.value

    if start.max_sum is not None:
        return start.max_sum

    left = dfs(start.left)
    right = dfs(start.right)
    start.max_sum = max(left, right) + start.value

    return start.max_sum

print dfs(tree[0])
