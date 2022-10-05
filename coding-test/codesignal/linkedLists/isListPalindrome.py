# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(l):
    s = []
    c = l
    while c:
        s.append(c.value)
        c = c.next
    return s == s[::-1]
