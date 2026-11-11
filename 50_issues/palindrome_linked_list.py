import pytest


# https://leetcode.com/problems/palindrome-linked-list/description/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        # We could store node values in a list, but that would require O(n) extra space.
        # Instead, use two pointers and in-place reversal to achieve O(1) extra space.

        # Find the middle using fast and slow pointers.

        # Reverse the second half in place.
        # Save the next node before changing the current node's next pointer.

        # Compare the first half with the reversed second half.

        fast, slow = head, head

        # find middle by slow
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half
        prev = None
        while slow:
            # prev -> slow -> next -> None
            # None <- slow <- next <- prev
            tmp = slow.next

            slow.next = prev
            prev = slow

            slow = tmp

        # check palindrome
        left, right = head, prev
        while right:
            # Compare only while right is not None, since we only need to check
            # the reversed second half, which may be shorter than the first half.
            # Example: 1 -> 2 -> 3 -> 2 -> 1
            # left:    1 -> 2 -> 3 -> None
            # right:   1 -> 2 -> 3 -> None
            # For even length: 1 -> 2 -> 2 -> 1
            # left:    1 -> 2 -> 2 -> None
            # right:   1 -> 2 -> None
            # Stop when right reaches None, since all required pairs have been compared.
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True


sol = Solution()
# time complexity O(n)
# memory complexity O(1)


head = ListNode(1,
                ListNode(2,
                         ListNode(2,
                                  ListNode(1)
                                  )
                         )
                )
head2 = ListNode(1,
                ListNode(2)
                )


@pytest.mark.parametrize(
    "head, expected",
    [
        (head, True),
        (head2, False),
    ]
)
def test_isPalindrome(head, expected):
    assert sol.isPalindrome(head) == expected
