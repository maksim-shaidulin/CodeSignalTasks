class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        for i, n1 in enumerate(num1[::-1]):
            tmp = 0
            for j, n2 in enumerate(num2[::-1]):
                tmp += int(n1) * int(n2) * 10**i * 10**j
            res += tmp
        return str(res)


def test_mupltiply():
    assert Solution().multiply("2", "12") == "24"
    assert Solution().multiply("1", "0") == "0"
    assert Solution().multiply("2", "6") == "12"
    assert Solution().multiply("123", "456") == "56088"


test_mupltiply()
"""
   123
   456
   ---
    18
   15
  12
+
   12
  10
  8
+
   6
  5
 4  
====
 55088
"""
