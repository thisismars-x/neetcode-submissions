# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True

        # lets do a preorder traversal

        def _preorder(pnode: TreeNode | None, qnode: TreeNode | None) -> bool:
            if not pnode and not qnode: return True
            if not pnode and qnode: return False
            if pnode and not qnode: return False
        
            return (pnode.val == qnode.val) and _preorder(pnode.left, qnode.left) and _preorder(pnode.right, qnode.right)

        return _preorder(p, q)