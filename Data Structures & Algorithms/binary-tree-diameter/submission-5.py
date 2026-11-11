# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        d = -float('inf')
        def _height(node: TreeNode | None):
            nonlocal d
            if not node:
                return 0

            lh, rh = _height(node.left), _height(node.right)
            d = max(d, lh + rh)
            return max(lh, rh) + 1

        _height(root)
        return d