from itertools import permutations
from itertools import islice

primes = [2, 3, 5, 7, 11, 13, 17]


def v1():
    def is_divisible(div, permutation, start):
        n = sum(i * exp for exp,
                i in zip([100, 10, 1], islice(permutation, start, start + 3)))
        return n % div == 0

    retval = []
    for permutation in permutations(xrange(10)):
        for div, start in zip(primes, xrange(1, 8)):
            if not is_divisible(div, permutation, start):
                break
        else:
            retval.append(permutation)
    return sum(int(''.join(str(i) for i in perm)) for perm in retval)
print v1()


def v2():
    def is_divisible(num, div):
        return num % div == 0

    def concat(num1, num2):
        return int("{0}{1}".format(num1, num2))

    def work(carry, nums, divisors):
        if len(nums) == 1:
            return list(i for i in nums)
        retval = []
        divisor, divisors = divisors[0], divisors[1:]
        for digit in nums:
            new_carry = carry + digit * 100
            if is_divisible(new_carry, divisor):
                retval.extend(concat(res, digit)
                              for res in work(new_carry / 10,
                                              nums - set([digit]),
                                              divisors))
        return retval

    def work_caller(nums, divisors):
        retval = []
        for i, j in permutations(xrange(10), 2):
            num = i * 10 + j
            retval.extend(concat(res, num)
                          for res in work(num,
                                          nums - set([i, j]),
                                          divisors))
        return retval

    nums = set(xrange(10))
    divisors = list(reversed(primes))
    retval = work_caller(nums, divisors)
    return sum(retval)
print v2()
