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
        # O(n) memory and O(nlogn) time
        res = []
        from bisect import insort
        def _inorder(node: TreeNode | None):
            if not node: return
            res.append(node.val)
            _inorder(node.left)
            _inorder(node.right)

        _inorder(root)
        res.sort()
        return res[k-1]

            
        