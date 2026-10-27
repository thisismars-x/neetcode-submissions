# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # get left height and right height and subtract
        # looks like a postorder traversal
        if not root: return True

        def _postorder(node: TreeNode | None) -> int:
            if not node: return 0

            left_height = _postorder(node.left)
            right_height = _postorder(node.right)
            if left_height == -1 or right_height == -1: return -1
            left_height += 1
            right_height += 1

            if abs(left_height - right_height) > 1:
                return -1

            return max(left_height, right_height)

        # return _postorder(root)
        if _postorder(root) == -1: return False
        return True