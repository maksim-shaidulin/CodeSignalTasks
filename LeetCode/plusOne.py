from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join([str(x) for x in digits])) + 1
        return [int(x) for x in str(num)]


def test_plusOne():
    assert Solution().plusOne([0]) == [1]
    assert Solution().plusOne([1]) == [2]
    assert Solution().plusOne([9]) == [1, 0]
    assert Solution().plusOne([1, 2]) == [1, 3]
    assert Solution().plusOne([9, 9]) == [1, 0, 0]
