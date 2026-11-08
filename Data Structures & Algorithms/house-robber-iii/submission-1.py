# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        from functools import cache
        
        @cache
        def _dfs(node: TreeNode | None):
            if not node:
                return 0

            res = node.val
            if node.left:
                res += _dfs(node.left.left) + _dfs(node.left.right)
            if node.right:
                res += _dfs(node.right.left) + _dfs(node.right.right)

            return max(
                res,
                _dfs(node.left) + _dfs(node.right)
            )

        return _dfs(root)

