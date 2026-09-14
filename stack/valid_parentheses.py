from typing import List


# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        # time O(s)
        # memory O(s)
        stack = []
        close_to_open = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        for c in s:
            if c in close_to_open:
                if stack and close_to_open[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return not stack # corner case for a "({[" input
