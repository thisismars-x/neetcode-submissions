# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        ## looks like a dfs/preorder traversal
        tc = 0
        def _inorder(node: TreeNode | None, cmax: int):
            if not node:
                return

            nonlocal tc
            if node.val >= cmax:
                tc += 1
            _inorder(node.left, max(cmax, node.val))
            _inorder(node.right, max(cmax, node.val))
        
        from sys import maxsize
        _inorder(root, -maxsize)
        return tc