# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3285/

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i, end_index = 0, len(nums) - 1
        while end_index > i:
            if nums[i] == 0:
                nums.append(0)
                del nums[i]
                end_index -= 1
            else:
                i += 1


sol = Solution()
arr = [0, 1, 0, 3, 12]
arr = [1, 2, 0, 0, 3, 4, 0, 5]
sol.maxSubArray(arr)
print(arr)
