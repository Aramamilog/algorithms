from typing import Optional

import pytest


# https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # FIRST DECISION OPTIMAL
        if not head:
            return head

        curr = head
        prev = None

        while curr:
            # save next
            curr_next = curr.next

            # reverse current
            curr.next = prev

            # shift pointers
            prev = curr
            curr = curr_next

        # return prev because it's the head of the reversed list now
        return prev

        # SECOND DECISION
        if not head:
            return head

        result_head = head  # if the linked list has only one node, it's the result head
        if head.next:
            result_head = self.reverseList(head.next)  # set the new result head that is deeper in the recursion
            head.next.next = head
            head.next = None  # set the self-next pointer to None
            # (for last the last node it's the same as it is, but it will be changed in the recursion from the upper level)

        return result_head


sol = Solution()
# FIRST DECISION
# time complexity O(n)
# memory complexity O(1)

# SECOND DECISION
# time complexity O(n)
# memory complexity O(h)

node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
expected_node = ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1)))))


def linked_list_to_list(head: Optional[ListNode]) -> list[int]:
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result


@pytest.mark.parametrize(
    "head, expected",
    [
        (node, [5,4,3,2,1]),
    ]
)
def test_reverseList(head, expected):
    result = sol.reverseList(head)
    assert linked_list_to_list(result) == expected


# SECOND DECISION: test limit of python recursion, has to raise RecursionError
def test_reverse_large_linked_list():
    size = 5000

    head = None

    # Build a linked list: 1 -> 2 -> ... -> 5000.
    for value in range(size, 0, -1):
        head = ListNode(value, head)

    result = Solution().reverseList(head)

    assert linked_list_to_list(result) == list(range(size, 0, -1))
