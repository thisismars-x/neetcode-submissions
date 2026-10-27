# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root

        # you  can do an inorder traversal too

        def _inorder(node: TreeNode | None):
            if not node: return

            node.left, node.right = node.right, node.left
            _inorder(node.left)
            _inorder(node.right)
        

        _inorder(root)
        return root