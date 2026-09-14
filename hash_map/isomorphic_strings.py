from typing import List


# https://leetcode.com/problems/isomorphic-strings/
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # time O(len(s/t)) = O(n)
        # memory O(len(s)+len(t)) = O(2n) = O(n)
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
