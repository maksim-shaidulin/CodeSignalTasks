class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.f(S) == self.f(T)

    def f(self, s):
        res = []
        for x in s:
            if x == "#":
                if res:
                    res.pop()
            else:
                res.append(x)
        return "".join(res)


sol = Solution()
sol.backspaceCompare('abc', 'abcd#') == True
sol.backspaceCompare('ab#c', 'ac') == True
sol.backspaceCompare('#', '') == True
sol.backspaceCompare('abc', 'abc') == True
sol.backspaceCompare('#abc##', 'a#a') == True
sol.backspaceCompare('#ab', '#ab###') == False
sol.backspaceCompare('a#b', '#d') == False
