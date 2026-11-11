# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        
        tc = 0
        def _dfs(node: TreeNode, cmax: int):
            nonlocal tc

            if node.val >= cmax:
                cmax = node.val
                tc += 1

            if node.left: _dfs(node.left, cmax)
            if node.right: _dfs(node.right, cmax)
            
        _dfs(root, -101)
        return tc
        