# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, height):
            if not node:
                return height
            left = dfs(node.left, height+1)
            right = dfs(node.right, height+1)
            if abs(left-right) > 1:
                ans[0] = False
            return max(left, right)
        if not root:
            return True
        ans = [True]
        dfs(root, 0)
        return ans[0]
        