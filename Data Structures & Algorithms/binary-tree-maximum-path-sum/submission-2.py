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

        ans = -float("inf")

        def _dfs(node: TreeNode | None) -> int:
            nonlocal ans
            if not node:
                return 0

            lsum = max(_dfs(node.left), 0)
            rsum = max(_dfs(node.right), 0)
            ans = max(ans, lsum + rsum + node.val)
            return node.val + max(lsum, rsum)

        _dfs(root)
        return ans





















        if not root: return 0

        # this also looks like a preorder traversal(dfs)
        res = -float("inf")

        def _dfs(node: TreeNode | None) -> int:
            nonlocal res
            if not node:
                return 0

            ls = max(0, _dfs(node.left))
            rs = max(0, _dfs(node.right))
            res = max(res, ls + rs + node.val)

            return node.val + max(ls, rs)

        _dfs(root)
        return res
        