import pytest


# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                last, prev = stack.pop(), stack.pop()
                stack.append(prev - last)
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '/':
                last, prev = stack.pop(), stack.pop()
                stack.append(int(prev / last))  # int to round to 0
            else:
                stack.append(int(c))

        return stack[0]


sol = Solution()
# time complexity O(n)
# memory complexity O(n)


@pytest.mark.parametrize(
    "tokens, expected",
    [
        (["2","1","+","3","*"], 9),
        (["4","13","5","/","+"], 6),
        (["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22)
    ]
)
def test_evalRPN(tokens, expected):
    assert sol.evalRPN(tokens) == expected
