# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3284/


class Solution:
    def isHappy(self, n: int) -> bool:
        used_nums = set()
        while True:
            n = sum((int(x) ** 2) for x in str(n))
            if n in used_nums:
                return False, n, used_nums
            if n == 1:
                return True, n, used_nums
            used_nums.add(n)


sol = Solution()
print(sol.isHappy(3))
print(sol.isHappy(3229))
