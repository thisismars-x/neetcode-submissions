# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def _same(node1: TreeNode | None, node2: TreeNode | None) -> bool:
            if not node1 and not node2:
                return True
            
            if not node1 and node2:
                return False
            
            if not node2 and node1:
                return False

            return node1.val == node2.val and _same(node1.left, node2.left) and _same(node1.right, node2.right)

        
        def _dfs(node: TreeNode | None) -> bool:
            if not node:
                return False

            if node.val == subRoot.val:
                if _same(node, subRoot):
                    return True

            if _dfs(node.left) or _dfs(node.right):
                return True

            return False

        return _dfs(root)