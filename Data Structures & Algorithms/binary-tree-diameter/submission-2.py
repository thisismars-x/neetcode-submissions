# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        # diameter = max_height of left_subtree + max_height of right_subtree + 1
        d = 0
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

























        if not root: return 0
        res = 0

        # lets do a inrorder traversal

        def _inorder(node: TreeNode | None) -> int:
            # this function will return max height
            nonlocal res
            if not node: return 0
            
            left_height = _inorder(node.left)
            right_height = _inorder(node.right) 

            res = max(res, left_height + right_height)
            return max(left_height, right_height) + 1

        _inorder(root)
        return res