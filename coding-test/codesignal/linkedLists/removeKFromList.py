# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next: ListNode = None
#
def solution(l: ListNode, k):
    if not l:
        return l
        
    dummy = ListNode(-1)
    dummy.next = l
    
    prev = dummy
    current = l
    while current:
        if current.value == k:
            # delete
            temp = current
            prev.next = current.next
            current = current.next
            del(temp)
        else:
            #traverse
            prev = prev.next
            current = current.next
    return dummy.next


# smart solution
def solution(l: ListNode, k):
    c = l
    while c:
        if c.next and c.next.value == k:
            c.next = c.next.next
        else:
            c = c.next
    return l.next if l and l.value == k else l