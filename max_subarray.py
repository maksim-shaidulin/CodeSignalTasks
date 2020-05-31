class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        max_total = max_cur = 0
        cur_arr = []
        max_arr = []
        for x in A:
            if x >= 0:
                max_cur += x
                cur_arr.append(x)
                if max_total == max_cur:
                    # same values, need to compare lengths
                    if len(cur_arr) > len(max_arr):
                        max_arr = cur_arr.copy()

                if max_cur > max_total:
                    max_total = max_cur
                    max_arr = cur_arr.copy()
            else:
                max_cur = 0
                cur_arr.clear()
        return max_arr


sol = Solution()
assert sol.maxset([1, 5, -1, 0, 7]) == [0, 7]
assert sol.maxset([-1, 1, 2, 3, -2, 3]) == [1, 2, 3]
assert sol.maxset([]) == []
assert sol.maxset([-1, -2]) == []
assert sol.maxset([-1, 0, 0, -2]) == [0, 0]
assert sol.maxset([0, 0, -1, 0]) == [0, 0]
