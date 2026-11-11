import pytest


# https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        l, r = 0, len(s) - 1
        while l <= r:
            l_valid, r_valid = s[l].isalnum(), s[r].isalnum()
            if not l_valid:
                l += 1
            if not r_valid:
                r -= 1

            if l_valid and r_valid:
                if s[l].lower() != s[r].lower():
                    return False
                else:
                    l += 1
                    r -= 1

        return True

sol = Solution()
# time complexity O(n)
# memory complexity O(1)


@pytest.mark.parametrize(
    "s, expected",
    [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
    ]
)
def test_isPalindrome(s, expected):
    assert sol.isPalindrome(s) == expected
