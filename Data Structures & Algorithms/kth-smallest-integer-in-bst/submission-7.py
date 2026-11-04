# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def _inorder(node: TreeNode | None, res: list[int]):
            if not node:
                return

            _inorder(node.left, res)
            res.append(node.val)
            _inorder(node.right, res)

        s = []
        _inorder(root, s)
        return s[k - 1]
        