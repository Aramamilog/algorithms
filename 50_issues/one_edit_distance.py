import pytest


# https://leetcode.com/problems/one-edit-distance/
# Premium or https://www.lintcode.com/problem/640/
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1:
            # have to do more than 1 operation because of length diff
            return False

        elif len(s) == len(t):
            # find replace possibility
            diff_count = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    diff_count += 1
            return diff_count == 1  # True there is 1 diff, False they are identical

        else:
            # find insert or delete possibility
            if len(s) > len(t):
                # make sure s is the shorter string
                s, t = t, s

            diff_count = 0
            s_p, t_p = 0, 0
            while s_p < len(s):
                if s[s_p] != t[t_p]:
                    diff_count += 1
                    if diff_count > 1:
                        return False

                    # skip one character in the longer string
                    t_p +=1
                    continue

                s_p +=1
                t_p +=1

            return True


sol = Solution()
# time complexity O(n + m)
# memory complexity O(1)


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("aDb", "adb", True),
        ("ab", "ab", False),
    ]
)
def test_isOneEditDistance(s, t, expected):
    assert sol.isOneEditDistance(s, t) == expected
