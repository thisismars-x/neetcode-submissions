# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        if not root: return 0

        # naive solution(build list)
        # O(n) memory and O(n) time
        res = []
        def _inorder(node: TreeNode | None):
            if len(res) == k: return
            if not node: return
            _inorder(node.left)
            res.append(node.val)
            _inorder(node.right)

        _inorder(root)
        return res[k-1]

            
        