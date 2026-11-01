# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if (not p and q) or (not q and p): return False

        # just go preorder
        def _dfs(pn: TreeNode | None, qn: TreeNode | None) -> bool:
            if (not pn and qn) or (not qn and pn): return False
            if not pn and not qn: return True

            if pn.val != qn.val: return False
            return _dfs(pn.left, qn.left) and _dfs(pn.right, qn.right)

        return _dfs(p, q)






        if not p and not q: return True

        # lets do a preorder traversal

        def _preorder(pnode: TreeNode | None, qnode: TreeNode | None) -> bool:
            if not pnode and not qnode: return True
            if not pnode and qnode: return False
            if pnode and not qnode: return False
        
            return (pnode.val == qnode.val) and _preorder(pnode.left, qnode.left) and _preorder(pnode.right, qnode.right)

        return _preorder(p, q)