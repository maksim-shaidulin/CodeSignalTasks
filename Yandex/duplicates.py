import sys
import math


def remove_duplicates(nums):
    res = []
    if not nums:
        return res
    last = nums[0]
    for num in nums:
        if num > last:
            last = num
            res.append(num)


count = int(sys.stdin.readline().strip())
res = []
max_n = -math.inf

for _ in range(count):
    n = int(sys.stdin.readline().strip())
    if n > max_n:
        res.append(n)
        max_n = n


for x in res:
    print(x)
