import pytest


# https://leetcode.com/problems/valid-palindrome-ii/description/
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skipL, skipR = s[l + 1:r + 1], s[l:r]
                return skipL == skipL[::-1] or skipR == skipR[:: -1]

            l += 1
            r -= 1

        return True



sol = Solution()
# time complexity O(n) + O(n) = O(2n) = O(n)
# memory complexity O(2n) = O(n) - but we can iterate by both skipL, skipR instead of reversing list to get O(1)


@pytest.mark.parametrize(
    "s, expected",
    [
        ("aba", True),
        ("abca", True),
        ("abc", False),
    ]
)
def test_validPalindrome(s, expected):
    assert sol.validPalindrome(s) == expected
