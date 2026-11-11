import pytest


# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        res_len = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res = s[l:r + 1]
                    res_len = r - l + 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res = s[l:r + 1]
                    res_len = r - l + 1
                l -= 1
                r += 1

        return res


sol = Solution()
# time complexity O(n^2)
# memory complexity O(n)


@pytest.mark.parametrize(
    "s,expected",
    [
        ("babad", ["aba", "bab"]),
        ("cbbd", "bb"),
    ],
)
def test_longestPalindrome(s, expected):
    assert sol.longestPalindrome(s) in expected
