#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def solution(t, k):
    kth = [0]
    value = [1000000]
    def backtrack(node):
        if not node or value[0] != 1000000: 
            return
        backtrack(node.left)
        kth[0] += 1
        if kth[0] == k:
            value[0] = node.value
        backtrack(node.right)      
                 
    backtrack(t)
    return value[0]


# Smart answer usung yield
# By AWice

def solution(root, K):
    def dfs(node):
        if node:
            yield from dfs(node.left)
            yield node.value
            yield from dfs(node.right)
    
    f = dfs(root)
    for _ in range(K):
        ans = next(f)
    return ans