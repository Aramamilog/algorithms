import pytest


# https://leetcode.com/problems/string-compression/description/
class Solution:
    def compress(self, chars: list[str]) -> int:
        insert = 0
        i = 0
        while i < len(chars):
            group = 1
            while (group + i) < len(chars) and chars[group + i] == chars[i]:
                group += 1

            chars[insert] = chars[i]
            insert += 1

            if group > 1:
                for digit in str(group):
                    chars[insert] = digit
                    insert += 1

                # or like this
                # string = str(group)
                # chars[insert: insert + len(string)] = list(string)
                # insert += len(string)

            i += group

        return insert


sol = Solution()
# time complexity O(n)
# memory complexity O(log n) because of str(group)
#   we can operate with digits by chr and ord to get memory O(1), but it way longer code


@pytest.mark.parametrize(
    "chars, expected",
    [
        (["a","a","b","b","c","c","c"], 6),
        (["a"], 1),
        (["a","b","b","b","b","b","b","b","b","b","b","b","b"], 4)
    ]
)
def test_compress(chars, expected):
    assert sol.compress(chars) == expected
