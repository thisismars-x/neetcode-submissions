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
            nonlocal res
            if not node:
                res.append('N')
                return

            res.append(str(node.val))
            _dfs(node.left)
            _dfs(node.right)

        _dfs(root)
        return ','.join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = iter(data.split(','))

        def _scan() -> TreeNode:
            nonlocal nodes

            value = next(nodes)
            if value == 'N':
                return None

            root = TreeNode(int(value))
            root.left = _scan()
            root.right = _scan()

            return root

        return _scan()



