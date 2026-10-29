import pytest


# https://leetcode.com/problems/restore-ip-addresses/
class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        res = []
        if len(s) > 12:
            return res

        def backtrack(i, dots, cur_IP):  # dfs algo
            if dots == 4 and i == len(s):
                res.append(cur_IP[:-1])
                return

            if dots > 4:
                return

            for j in range(i, min(i + 3, len(s))):
                IP_val = s[i:j + 1]
                if int(IP_val) < 256 and (i == j or s[i] != '0'):
                    # i == j: A single-digit segment is valid, including "0".
                    # s[i] != '0': Multi-digit segments must not have leading zeros.
                    backtrack(j + 1, dots + 1, cur_IP + IP_val + '.')

        backtrack(0, 0, '')

        return res


sol = Solution()
# Time: O(3^4) = O(1)
# Each segment has at most 3 choices (1, 2, or 3 digits),
# and a valid IP address consists of exactly 4 segments.

# Memory: O(5) = O(1)
# Maximum recursion depth is 5: 1 initial call + 4 calls
# for the IP segments.


@pytest.mark.parametrize(
    "s, expected",
    [
        ("25525511135", ["255.255.11.135","255.255.111.35"]),
        ("0000", ["0.0.0.0"]),
        ("101023",["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]),
     ],
)
def test_restoreIpAddresses(s, expected):
    assert sol.restoreIpAddresses(s) == expected
