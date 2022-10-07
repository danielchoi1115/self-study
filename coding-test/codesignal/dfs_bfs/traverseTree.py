#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def solution(t):
    
    to_visit = [t]
    visited = []
    while to_visit:
        temp = []
        for node in to_visit:
            if not node:
                continue
            visited.append(node.value)
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        to_visit = temp
    return visited
    
            