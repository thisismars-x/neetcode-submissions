# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # preorder traversal

        tc = 0
        def _dfs(node: TreeNode | None, cmax: int):
            nonlocal tc
            if not node:
                return

            tc += 1 if node.val >= cmax else 0
            cmax = max(node.val, cmax)
            _dfs(node.left, cmax)
            _dfs(node.right, cmax)

        _dfs(root, -float('inf'))
        return tc
        