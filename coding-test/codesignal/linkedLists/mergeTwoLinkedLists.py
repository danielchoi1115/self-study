# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next: ListNode = None

def solution(l1, l2):
    dummy = ListNode(-1)
    
    current = dummy
    p1 = l1
    p2 = l2
    
    while p1 or p2:
        if not p1:
            current.next = p2
            p2 = None
        elif not p2:
            current.next = p1
            p1 = None
        else:
            if p1.value <= p2.value:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            current = current.next
    return dummy.next


# more neat answer
def solution(A, B):
    cur = ans = ListNode(None)
    
    while A and B:
        if A.value <= B.value:
            cur.next = cur = ListNode(A.value)
            A = A.next
        else:
            cur.next = cur = ListNode(B.value)
            B = B.next
    
    cur.next = A or B
    return ans.next
