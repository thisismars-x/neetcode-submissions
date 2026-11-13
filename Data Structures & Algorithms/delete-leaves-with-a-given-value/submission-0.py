# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def _dfs(node: TreeNode | None) -> TreeNode | None:
            if not node:
                return None
                
            node.left = _dfs(node.left)
            node.right = _dfs(node.right)

            if not (node.left or node.right) and node.val == target:
                return None

            return node

        return _dfs(root)
        