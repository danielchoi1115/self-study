#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

# Failed to solve...
# Copied from geeksforgeeks
# https://www.geeksforgeeks.org/check-if-a-binary-tree-is-subtree-of-another-binary-tree/

def solution(root1, root2):
    def areIdentical(root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
            
        return (root1.value == root2.value) and \
                areIdentical(root1.left, root2.left) and \
                areIdentical(root1.right, root2.right)
    def isSubtree(root1, root2):
        if root2 is None:
            return True
        if root1 is None:
            return False
        
        if areIdentical(root1, root2):
            return True
        
        return isSubtree(root1.left, root2) or isSubtree(root1.right, root2)
    return isSubtree(root1, root2)