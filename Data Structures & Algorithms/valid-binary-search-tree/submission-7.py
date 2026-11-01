# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # is left and right subtree balanced/?
        if not root: return True

        def _dfs(node: TreeNode | None, l: int, r: int) -> bool:
            if not node: return True
            if not (l < node.val < r): return False
            return _dfs(node.left, l, node.val) and _dfs(node.right, node.val, r)


        return _dfs(root, -float("inf"), +float("inf"))















        def _valid(node, l, r):
            if not node: return True
            if not (l < node.val < r): return False
            return _valid(node.left, l, node.val) and _valid(node.right, node.val, r)

        from sys import maxsize
        return _valid(root, -maxsize, maxsize)