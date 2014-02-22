def genlist(nums, lsts):
    if not nums:
        return lsts

    top = nums.pop()
    retval = []
    for lst in lsts:
        for i in range(len(lst)):
            if lst[i] is None:
                copy = list(lst)
                copy[i] = top
                retval.extend(genlist(list(nums), [copy]))
    return retval


up_to = 10
t = genlist(range(0, up_to), [[None] * up_to])

print sorted(t)[1000000 - 1]
