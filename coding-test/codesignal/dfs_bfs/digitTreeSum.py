#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def solution(t):
    numbers = []
    def dfs(node, val):
        if not node:
            return
        if node.left is None and node.right is None:
            numbers.append(val + str(node.value))
            return
        else:
            dfs(node.left, val + str(node.value))
            dfs(node.right, val + str(node.value))
    dfs(t, '')
    return sum([int(n) for n in numbers])


# more Mathematical solution using digit multiplication
# by AWice
def solution(t, s = 0):
    if not t:
        return 0
    if t and not t.left and not t.right:
        return 10*s + t.value
    return (solution(t.left, 10*s + t.value) +
            solution(t.right, 10*s + t.value))