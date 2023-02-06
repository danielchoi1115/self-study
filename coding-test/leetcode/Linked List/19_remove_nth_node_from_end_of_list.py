# https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Solve with Two pointers


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = head
        r = head
        for i in range(n):
            r = r.next
        temp = None
        while r:
            temp = l
            l = l.next
            r = r.next

        if temp is None:
            return l.next
            
        temp.next = l.next
        return head