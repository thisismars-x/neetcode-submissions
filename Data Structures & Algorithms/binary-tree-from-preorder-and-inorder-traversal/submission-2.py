# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        index = {c:i for i,c in enumerate(inorder)}

        root_index = 0
        def _dfs(l: int, r: int):
            if l > r:
                return
            nonlocal root_index
            root_node_val = preorder[root_index]
            root_index += 1

            mid = index[root_node_val]
            root_node = TreeNode(root_node_val)
            root_node.left = _dfs(l, mid - 1)
            root_node.right = _dfs(mid + 1, r)
            return root_node

        return _dfs(0, len(preorder) - 1)

        