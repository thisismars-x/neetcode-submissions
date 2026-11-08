# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        def _pt(node: TreeNode | None):
            if not node:
                return 

            _pt(node.left)
            _pt(node.right)
            res.append(node.val)

        _pt(root)
        return res