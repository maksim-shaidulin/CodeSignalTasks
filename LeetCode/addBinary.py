# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # first = int(a, 2)
        # second = int(b, 2)
        # sum = first + second
        # result = "{0:b}".format(sum)
        # return result
        return "{0:b}".format(int(a, 2) + int(b, 2))

def test_addBinary():
    assert Solution().addBinary("0", "0") == "0"
    assert Solution().addBinary("11", "1") == "100"
    assert Solution().addBinary("1010", "1011") == "10101"