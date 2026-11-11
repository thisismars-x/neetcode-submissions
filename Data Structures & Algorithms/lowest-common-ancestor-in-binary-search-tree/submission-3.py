# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        res = root
        while True:
            if res.val < p.val and res.val < q.val:
                res = res.right
            elif res.val > p.val and res.val > q.val:
                res = res.left
            else:
                return res
        