# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:



        # when doing dfs scan rememebr the max value along curr path
        OOR = -101

        tc = 0
        def _dfs(node: TreeNode | None, cm: int):
            nonlocal tc

            if not node:
                return

            if node.val >= cm:
                tc += 1
                cm = node.val

            _dfs(node.left, cm)
            _dfs(node.right, cm)

        _dfs(root, OOR)
        return tc















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