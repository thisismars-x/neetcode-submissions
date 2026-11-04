# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        md = 0
        def _height(node: TreeNode | None) -> int:
            nonlocal md
            if not node:
                return 0

            lh = _height(node.left)
            rh = _height(node.right)
            md = max(md, lh + rh)
            return max(lh, rh) + 1
        
        _height(root)
        return md