#
# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None
def solution(inorder, preorder):

    def restore(inorder: list, preorder: list):
        if not preorder:
            return None
        # preorder[0] is always the root value
        rt_val = preorder[0]
        # find root from inorder and slice it to get left, right subtree
        in_rt = inorder.index(rt_val)
        in_l = inorder[:in_rt]
        in_r = inorder[in_rt+1:]
        # according to the length of inorder subtrees, get preorder subtrees
        pre_l = preorder[1:1+len(in_l)]
        pre_r = preorder[1+len(in_l):1+len(in_l)+len(in_r)]
        
        root = Tree(rt_val)
        root.left = restore(in_l, pre_l)
        root.right = restore(in_r, pre_r)
        
        return root
        
        
    return restore(inorder, preorder)


# Same concept but more compact solution
# by thaumkid
def solution(inorder, preorder):
  if not preorder:
    return None
  root = Tree(preorder[0])
  i = inorder.index(preorder[0])
  root.left = solution(inorder[:i], preorder[1:i+1])
  root.right = solution(inorder[i+1:],preorder[i+1:])
  return root