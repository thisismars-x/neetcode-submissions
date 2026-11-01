# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot: return True
        if root and not subRoot: return True 
        if not root and subRoot: return False

        # subtree is when the val at node is equal and left and right subtree are both equal
        def _same(n1: TreeNode | None, n2: TreeNode | None) -> bool:
            if not n1 and not n2: return True
            if (not n1 and n2) or (not n2 and n1): return False
            if n1.val != n2.val: return False
            return _same(n1.left, n2.left) and _same(n1.right, n2.right)

        # now preorder traversal and if node matches chefcl for same tree
        def _dfs(node: TreeNode | None) -> bool:
            if not node: return False

            if node.val == subRoot.val:
                if _same(node, subRoot):
                    return True

            l = _dfs(node.left)
            r = _dfs(node.right)
            if l or r:
                return True
            return False

        
        return _dfs(root)

















        if not subRoot: return True
        if not root: return False

        if self._same_tree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def _same_tree(self, r: TreeNode | None, s: TreeNode | None) -> bool:
        if not r and not s: return True
        if r and s and r.val == s.val:
            return self._same_tree(r.left, s.left) and self._same_tree(r.right, s.right)
        return False

        