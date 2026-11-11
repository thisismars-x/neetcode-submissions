# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        table = {n: i for i, n in enumerate(inorder)}
        
        root_inx = 0
        def _dfs(l: int, r: int):
            if l > r:
                return None
            nonlocal root_inx

            root_val = preorder[root_inx]
            root_inx += 1

            root_node = TreeNode(root_val)
            mid = table[root_val]
            root_node.left = _dfs(l, mid - 1)
            root_node.right = _dfs(mid + 1, r)

            return root_node

        return _dfs(0, len(preorder) - 1)