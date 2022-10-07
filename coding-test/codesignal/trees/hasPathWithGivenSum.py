#
# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None
def solution(t: Tree, s):
    def backtrack(node: Tree, val) -> bool:
        if node is None:
            return False
        if node.left == node.right == None:
            return (val + node.value) == s
        else:
            return backtrack(node.left, val + node.value) or backtrack(node.right, val + node.value)
    return backtrack(t, 0)



# Shorter solution using subtraction method
# by rynld
def solution(t: Tree, s):
    if t is None:
        return s == 0
    return solution(t.left, s - t.value) or solution(t.right, s - t.value)