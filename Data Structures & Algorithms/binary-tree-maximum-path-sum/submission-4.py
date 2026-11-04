# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_sum = -float('inf')
        def _dfs(node: int) -> int:
            nonlocal max_sum
            if not node:
                return 0

            lsum = max(0, _dfs(node.left))
            rsum = max(0, _dfs(node.right))
            max_sum = max(lsum + rsum + node.val, max_sum)
            return max(lsum, rsum) + node.val

        _dfs(root)
        return max_sum
        