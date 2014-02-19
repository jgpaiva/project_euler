
sum = 0
for i in str(2 ** 1000):
    if i.isspace():
        continue
    sum += int(i)
print sum
