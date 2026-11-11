# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def _dfs(node: TreeNode | None):
            if not node:
                res.append('X')
                return

            res.append(str(node.val))
            _dfs(node.left)
            _dfs(node.right)

        _dfs(root)
        return 'Y'.join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = iter(data.split('Y'))

        def _scan():
            nonlocal nodes

            node = next(nodes)
            if node == 'X':
                return None

            root = TreeNode(node)
            root.left, root.right = _scan(), _scan()
            return root

        return _scan()
