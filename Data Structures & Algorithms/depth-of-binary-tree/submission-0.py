# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # first you need maxdepth on left side, then on right side
        # then your answer is maxdepth(left, right) + 1?
        # looks like a postorder traversal?
        if not root: return 0

        def _postorder(node: TreeNode | None) -> int:
            if not node: return 0
        
            left_height = 1 + _postorder(node.left)
            right_height = 1 + _postorder(node.right)
            return max(left_height, right_height)

        return _postorder(root)