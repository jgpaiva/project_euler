limit = 1000000


def ispalindrome(num):
    for i, j in zip(num, reversed(num)):
        if i != j:
            return False
    else:
        return True

palindromes = []
for i in xrange(limit):
    if i % 2 == 0:  # only off numbers have '1' in the end
        continue
    if ispalindrome(str(i)) and ispalindrome(bin(i)[2:]):
        palindromes.append(i)
print palindromes
print sum(palindromes)
