from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head2 = ListNode(0)
        while head:
            nxt = head.next
            head.next = head2.next
            head2.next = head
            head = nxt
        return head2.next