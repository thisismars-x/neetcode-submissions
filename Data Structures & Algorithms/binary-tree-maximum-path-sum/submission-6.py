# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_sum = -float('inf')

        def _dfs(node: TreeNode | None):
            if not node:
                return 0

            lsum, rsum = max(0, _dfs(node.left)), max(0, _dfs(node.right))

            nonlocal max_sum
            max_sum = max(max_sum, lsum + rsum + node.val)
            return max(lsum, rsum) + node.val

        _dfs(root)
        return max_sum