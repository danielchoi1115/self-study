# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> int:
            if node is None:
                return [0, 0]

            left = dfs(node.left)
            right = dfs(node.right)

            with_root = node.val + left[1] + right[1]
            without_root = max(left) + max(right)

            return [with_root, without_root]
        return max(dfs(root))


itemList = [3, 2, 3, None, 3, None, 1]
# itemList = [3, 4, 5, 1, 3, None, 1]
itemList = [4, 1, None, 2, None, 3]

root = TreeNode(itemList[0])
root.left = TreeNode(itemList[1]) if itemList[1] is not None else None
root.right = TreeNode(itemList[2]) if itemList[2] is not None else None
root.left.left = TreeNode(itemList[3]) if itemList[3] is not None else None
root.left.right = TreeNode(itemList[4]) if itemList[4] is not None else None
root.right.left = TreeNode(itemList[5]) if itemList[5] is not None else None
root.right.right = TreeNode(itemList[6]) if itemList[6] is not None else None

s = Solution()
print(s.rob(root))
