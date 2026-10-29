import pytest


# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/
# Premium or https://www.lintcode.com/problem/386/solution
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        res = 0
        counts = {}

        l = 0
        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1

            while len(counts) > k:
                counts[s[l]] -= 1

                if counts[s[l]] == 0:
                    del counts[s[l]]

                l += 1

            res = max(res, r - l + 1)

        return res


sol = Solution()
# time complexity O(n)
# memory complexity O(k)


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("eceba", 3,4),
        ("WORLD", 4, 4)
    ]
)
def test_lengthOfLongestSubstringKDistinct(s, k, expected):
    assert sol.lengthOfLongestSubstringKDistinct(s, k) == expected
