from typing import List


# https://leetcode.com/problems/permutation-in-string/description/
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_map, s2_map = {}, {}

        for i in range(len(s1)):
            s1_map[s1[i]] = 1 + s1_map.get(s1[i], 0)
            s2_map[s2[i]] = 1 + s2_map.get(s2[i], 0)

        if s1_map == s2_map:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            s2_map[s2[r]] = 1 + s2_map.get(s2[r], 0)

            s2_map[s2[l]] -= 1
            if s2_map[s2[l]] == 0:
                del s2_map[s2[l]]

            if s1_map == s2_map:
                return True

            l += 1

        return False


sol = Solution()
assert sol.checkInclusion("ab", "eidbaooo") == True
assert sol.checkInclusion("ab", "eidboaoo") == False
# time complexity O(n)
# memory complexity O(len(s1)) + O(len(s2)) = O(c)
