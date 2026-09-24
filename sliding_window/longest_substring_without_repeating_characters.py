from typing import List


# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        res = 0
        l = 0

        for r in range(len(s)):
            while s[r] in chars:
                # while there is repeating char we have to move the left pointer
                # because we have to remove our repeating char from the set 'chars'
                # so we are moving the left pointer until we find the repeating char
                # and remove it
                chars.remove(s[l])
                l += 1

            chars.add(s[r])
            res = max(res, len(chars))  # also we can use (r - l + 1) as the window size instead of len(chars)

        return res


sol = Solution()
assert sol.lengthOfLongestSubstring("abcabcbb") == 3
assert sol.lengthOfLongestSubstring("bbbbb") == 1
assert sol.lengthOfLongestSubstring("pwwkew") == 3
# time complexity O(n)
# memory complexity O(len(s)) = O(c)
