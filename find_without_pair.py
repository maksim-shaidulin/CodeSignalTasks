from collections import Counter


def func(nums):
    d = Counter(nums)
    for item in d:
        if d[item] % 2 == 1:
            return item


assert func([3, 3, 3, 3, 3, 1, 1]) == 3
assert (func([3, 3, 5, 3, 3, 1, 1])) == 5
assert (func([1])) == 1
assert (func([3, 1, 1])) == 3
assert (func([1, 4, 8, 1, 5, 4, 8])) == 5
