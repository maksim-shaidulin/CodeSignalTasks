from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        while strs:
            first = strs[0]
            res.append(list(v for v in strs if sorted(v) == sorted(first)))
            strs = (list(v for v in strs if sorted(v) != sorted(first)))

        return res
        # ans = collections.defaultdict(list)
        # for s in strs:
        #     ans[tuple(sorted(s))].append(s)
        # return ans.values()


if __name__ == "__main__":
    a=[]
    b=[]
    a.remove(b)
