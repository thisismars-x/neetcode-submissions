# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        table = {n:i for i, n in enumerate(inorder)}

        curr_root = 0

        def _dfs(l: int, r: int):
            nonlocal curr_root
            if l > r:
                return None

            root_val = preorder[curr_root]
            curr_root += 1
            root_node = TreeNode(root_val)

            index = table[root_val]
            root_node.left = _dfs(l, index - 1)
            root_node.right = _dfs(index + 1, r)
            return root_node
        

        return _dfs(0, len(inorder) - 1)