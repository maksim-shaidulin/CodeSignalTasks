def func(nums):
    best = 0
    current = 0

    for num in nums:
        if num > 0:
            current += 1
            best = max(best, current)
        else:
            current = 0
    return best


if __name__ == "__main__":
    assert func([1]) == 1
    assert func([]) == 0
    assert func([1, 1, 1, 1]) == 4
    assert func([1, 1, 0, 1]) == 2
    assert func([0, 1, 1, 0, 1, 1, 1]) == 3
    assert func([0, 0, 0]) == 0
