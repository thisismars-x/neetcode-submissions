# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

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

        