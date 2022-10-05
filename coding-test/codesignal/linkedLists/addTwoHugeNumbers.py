# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(a, b):
    a_total = ''
    b_total = ''
    
    # traverse and get files
    while a:
        a_total += str(a.value).zfill(4)
        a = a.next
    while b:
        b_total += str(b.value).zfill(4)
        b = b.next
    
    sum_ = int(a_total) + int(b_total)
    
    sum_ = str(sum_)
    
    first_len = len(sum_) % 4 if len(sum_) % 4 != 0 else 4
    # cut first number
    res = [int(sum_[:first_len])]
    sum_ = sum_[first_len:]
    # add the rest
    for i in range(0, len(sum_), 4):
        res.append(int(sum_[i: i+4]))
    return res
    