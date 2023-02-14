# https://leetcode.com/problems/add-two-numbers/

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        carry = 0
        temp = head
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum_ = val1 + val2 + carry
            if sum_ > 9: 
                sum_ -= 10
                carry = 1
            else:
                carry = 0
            temp.next = ListNode(sum_)
            temp = temp.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry:
            temp.next = ListNode(1)
        return head.next

        