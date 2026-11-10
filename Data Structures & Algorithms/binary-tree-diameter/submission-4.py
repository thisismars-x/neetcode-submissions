# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        d = -float('inf')
        def _height(node: TreeNode | None) -> int:
            nonlocal d
            if not node:
                return 0

            lh = _height(node.left)
            rh = _height(node.right)

            d = max(d, lh + rh)
            return max(lh, rh) + 1

        _height(root)
        return d
        