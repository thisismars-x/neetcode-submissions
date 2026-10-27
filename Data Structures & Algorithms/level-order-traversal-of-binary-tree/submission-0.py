# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = []

        from collections import deque
        d = deque((root,))

        while d:
            tmp = []
            for _ in range(len(d)):
                node = d.popleft()
                tmp.append(node.val)
                if node.left: d.append(node.left)
                if node.right: d.append(node.right)
            res.append(tmp)

        return res