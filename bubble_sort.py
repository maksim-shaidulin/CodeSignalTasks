def bubble(nums):
    while True:
        sorted = True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                sorted = False
        if sorted:
            return nums



data = [
    [[6, 3, 9, 1, 7, 2], [1, 2, 3, 6, 7, 9]],
    [[1, 1, 1], [1, 1, 1]],
    [[], []],
    [[1], [1]],
    [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]],
]

for d in data:
    assert bubble(d[0]) == d[1]
# assert bubble([6, 3, 9, 1, 7, 2]) == [1, 2, 3, 6, 7, 9]
# assert bubble([1, 1, 1]) == [1, 1, 1]
# assert bubble([1]) == [1]
# assert bubble([]) == []
# assert bubble([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
