# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        max_sum = -float('inf')
        def _dfs(node: TreeNode | None) -> int:
            nonlocal max_sum
            if not node:
                return 0

            lh = max(0, _dfs(node.left))
            rh = max(0, _dfs(node.right))
            max_sum = max(lh + rh + node.val, max_sum)
            return max(lh, rh) + node.val

        _dfs(root)
        return max_sum
        