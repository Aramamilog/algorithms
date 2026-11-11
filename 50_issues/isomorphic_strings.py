from typing import List


# https://leetcode.com/problems/isomorphic-strings/
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_map_s = {}
        hash_map_t = {}
        for sc, tc in zip(s, t):
            if sc in hash_map_s:
                if hash_map_s[sc] != tc:
                    return False

            elif tc in hash_map_t:
                if hash_map_t[tc] != sc:
                    return False

            else:
                hash_map_s[sc] = tc
                hash_map_t[tc] = sc

        return True


sol = Solution()
assert sol.isIsomorphic("egg", "add") == True
assert sol.isIsomorphic("foo", "bar") == False
assert sol.isIsomorphic("paper", "title") == True
# time complexity O(len(s/t)) = O(n)
# memory complexity O(len(s)+len(t)) = O(2n) = O(n)
