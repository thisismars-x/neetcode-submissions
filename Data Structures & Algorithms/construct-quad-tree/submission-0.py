"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def _dfs(n: int, r: int, c: int):
            if n == 1:
                return Node(grid[r][c] == 1, True)
                
            mid = n // 2
            tl = _dfs(mid, r, c)
            tr = _dfs(mid, r, c + mid)
            bl = _dfs(mid, r + mid, c)
            br = _dfs(mid, r + mid, c + mid)

            if (
                all(x.isLeaf for x in (tl, tr, bl, br)) and
                tl.val == tr.val == bl.val == br.val
            ):
                return Node(tl.val, True)

            return Node(False, False, tl, tr, bl, br)

        return _dfs(len(grid), 0, 0)
