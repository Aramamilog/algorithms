from typing import List


# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):  # corner case
            return []

        p_count = {}
        s_count = {}

        for i in range(len(p)):
            p_count[p[i]] = 1 + p_count.get(p[i], 0)
            s_count[s[i]] = 1 + s_count.get(s[i], 0)
            # creating first s_count by p_count indexes to check corner case for the first chars

        res = []
        if p_count == s_count:  # corner case for the first chars as was talking above
            res.append(0)

        # sliding window
        l = 0
        for r in range(len(p), len(s)):
            s_count[s[l]] -= 1
            if s_count[s[l]] == 0:
                s_count.pop(s[l])
            l += 1

            s_count[s[r]] = 1 + s_count.get(s[r], 0)
            if p_count == s_count:
                res.append(l)

        return res


sol = Solution()
assert sol.findAnagrams("cbaebabacd", "abc") == [0,6]
assert sol.findAnagrams("abab", "ab") == [0,1,2]
# time complexity O(n)
# memory complexity O(len(s)) = O(c)
