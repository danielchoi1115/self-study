# https://leetcode.com/problems/sort-list/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# import heapq
# class Solution:
#     def sortList(self, head: ListNode) -> ListNode:
#         if head is None: return head
#         heap = []
#         i = 0
#         while head:
#             heapq.heappush(heap, (head.val, i, head))
#             i += 1
#             head = head.next
#         newHead = cur = heapq.heappop(heap)[2]
#         while heap:
#             cur.next = heapq.heappop(heap)[2]
#             cur = cur.next
#         cur.next = None

#         return newHead

# 200% smarter solution, no need to actually change the nodes. You just need to change the values.
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None: return head
        heap = []
        temp = head
        while temp:
            heap.append(temp.val)
            temp = temp.next
        heap.sort()
        cur = head
        for v in heap:
            cur.val = v
            cur = cur.next

        return head

h = ListNode(4)
temp = h
for v in [19,14,5,-3,1,8,5,11,15]:
    temp.next = ListNode(v)
    temp = temp.next

s = Solution()
ans = s.sortList(h)

while ans:
    print(ans.val, end=", ")
    ans = ans.next