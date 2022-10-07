#
# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None
def solution(t):
    left = []
    right = []
    def backtrack(node: Tree, l, side):
        if side == 'l':
            left = 'l'
            right = 'r'
        else:
            left = 'r'
            right = 'l'
        if node is None:
            return
        if node.left == node.right == None:
            l.append(node.value)
        elif node.left is None:
            l.append(left)
            backtrack(node.right, l, side)
        elif node.right is None:
            l.append(right)
            backtrack(node.left, l, side)
        else:
            l.append(node.value)
            if side == 'l':
                backtrack(node.left, l, side)
                backtrack(node.right, l, side)
            else:
                backtrack(node.right, l, side)
                backtrack(node.left, l, side)
    if t is None:
        return True
    backtrack(t.left, left, 'l')
    backtrack(t.right, right, 'r')

    return left == right


# Shorter solution by vantagexd
def solution(t):
    def mirrorEquals(left,right):
        if left is None or right is None:
            return left == None and right == None
        return left.value == right.value and \
               mirrorEquals(left.left, right.right) and \
               mirrorEquals(left.right, right.left)
    return mirrorEquals(t,t)
            