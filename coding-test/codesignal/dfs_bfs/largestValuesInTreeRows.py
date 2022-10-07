#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def solution(t):
    to_visit = [t]
    res = []
    while to_visit:
        temp = []
        largest = -9999
        for node in to_visit:
            if node is None:
                continue
            largest = node.value if node.value > largest else largest
            temp.append(node.right)
            temp.append(node.left)
        if largest > -9999:
            res.append(largest)
        to_visit = temp
    return res