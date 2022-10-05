# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def solution(l: ListNode, k):
    dummy = ListNode(None)
    dummy.next = l
    
    prev = dummy
    current = l
    temp = current
    stack = []
    while current:
        if len(stack) < k:
            if temp:
                stack.append(temp)
                temp = temp.next
            else:
                prev.next = current
                break
                
        if len(stack) == k:
            for n in stack[::-1]:
                prev.next = n
                prev = prev.next
            stack = []
            current = temp
            prev.next = current

                
    return dummy.next            