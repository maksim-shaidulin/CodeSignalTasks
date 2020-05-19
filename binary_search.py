assert bin_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4) == 4
def bin_search(nums, n):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] >= n:
            right = mid
        else:
            left = mid + 1
    return right if nums[right] == n else -1


assert bin_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == 3
assert bin_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9) == 9
assert bin_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0) == 0
assert bin_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10) == -1
assert bin_search([0, 1, 2, 3, 4, 5, 7, 8, 9], 6) == -1

