class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        r, c = len(grid), len(grid[0])

        from functools import cache

        @cache
        def _mps(i: int, j: int) -> int:
            if (i, j) == (r - 1, c - 1):
                return grid[i][j]

            cost = float('inf')
            for di, dj in ((0, 1), (1, 0)):
                i2, j2 = i + di, j + dj
                if 0 <= i2 < r and 0 <= j2 < c:
                    cost = min(cost, _mps(i2, j2))

            return cost + grid[i][j]

        return _mps(0, 0)
