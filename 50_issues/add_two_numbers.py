from typing import Optional

import pytest


# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_node = ListNode()
        head = result_node
        carry = 0

        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            sum_val = l1_val + l2_val + carry
            carry = sum_val // 10
            dig = sum_val % 10

            head.next = ListNode(dig)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            head = head.next

        return result_node.next



sol = Solution()
# time complexity O(n)
# memory complexity O(1)

l1_node = ListNode(2, ListNode(4, ListNode(3)))
l2_node = ListNode(5, ListNode(6, ListNode(4)))

def linked_list_to_list(head: Optional[ListNode]) -> list[int]:
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result


@pytest.mark.parametrize(
    "l1, l2, expected",
    [
        (l1_node, l2_node, [7, 0, 8]),
    ],
)
def test_addTwoNumbers(l1, l2, expected):
    result = sol.addTwoNumbers(l1, l2)
    assert linked_list_to_list(result) == expected
