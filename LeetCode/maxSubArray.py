from typing import List


class Solution:
    def maxSubArray(self, nums):
        if not nums:
            return 0

        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum
    def maxSubArray2(self, nums: List[int]) -> int:
        max_sum = None
        for i, v in enumerate(nums):
            cur_sum = v
            tmp = v
            for j in nums[i + 1 :]:
                tmp += j
                if cur_sum < tmp:
                    cur_sum = tmp
            if max_sum is None or cur_sum > max_sum:
                max_sum = cur_sum
        return max_sum


if __name__ == "__main__":
    sol = Solution()
    res = sol.maxSubArray([-5, 4, -1, -1, 3])
    # res = sol.maxSubArray([1,-3,2,3])
    print(res)
