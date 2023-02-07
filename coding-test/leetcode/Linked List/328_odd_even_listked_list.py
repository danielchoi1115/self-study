# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head

        odd = head
        even = evenHead = head.next

        isOdd = True
        while odd.next and even.next:
            if isOdd:
                odd.next = even.next
                odd = odd.next
            else:
                even.next = odd.next
                even = even.next
            isOdd = not isOdd
        if even:
            even.next = None
        odd.next = evenHead

        return head