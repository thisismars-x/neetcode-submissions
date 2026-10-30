# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: return ''
        res = []

        # preorder
        def _dfs(node: TreeNode | None):
            if not node:
                res.append('x')
                return
            res.append(str(node.val))
            _dfs(node.left)
            _dfs(node.right)
        
        _dfs(root)
        return ','.join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data: return None
        v = data.split(',')

        i = 0
        def _dfs():
            nonlocal i
            if v[i] == 'x':
                i += 1
                return None

            node = TreeNode(int(v[i]))
            i += 1
            node.left = _dfs()
            node.right = _dfs()
            return node

        return _dfs()