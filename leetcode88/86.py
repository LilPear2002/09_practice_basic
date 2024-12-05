from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        p1 = ListNode(0)
        p2 = ListNode(0)
        l1 = p1
        l2 = p2
        while head:
            if head.val < x:
                p1.next = head
                p1 = p1.next
                head = head.next
            else:
                p2.next = head
                p2 = p2.next
                head = head.next
        p1.next = l2.next
        p2.next = None
        return l1.next



