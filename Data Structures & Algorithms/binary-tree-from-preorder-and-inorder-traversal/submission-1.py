# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:


        t = {x:y for y,x in enumerate(inorder)}
        ri = 0

        def _scan(l: int, r: int) -> TreeNode | None:
            nonlocal ri
            if l > r: return None
            rval = preorder[ri]
            ri += 1
            root = TreeNode(rval)
            root.left, root.right = _scan(l, t[rval] - 1), _scan(t[rval] + 1, r)
            return root

        return _scan(0, len(preorder) - 1)



















        table = {v:i for i, v in enumerate(inorder)}

        pre_idx = 0
        def _inorder(l: int, r: int):
            nonlocal pre_idx
            if l > r: return None
            rval = preorder[pre_idx]
            pre_idx += 1

            root = TreeNode(rval)
            mid = table[rval]
            root.left, root.right = _inorder(l, mid-1), _inorder(mid+1, r)
            return root

        return _inorder(0, len(preorder) - 1)


        