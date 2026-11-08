class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid
        if grid[0][0] or grid[-1][-1]:
            return 0
        
        r, c = len(grid), len(grid[0])

        from functools import cache

        @cache
        def _upwo(i: int, j: int):
            if (i, j) == (r - 1, c - 1):
                return 1


            ways = 0
            if i + 1 < r and grid[i + 1][j] == 0:
                ways += _upwo(i + 1, j)

            if j + 1 < c and grid[i][j + 1] == 0:
                ways += _upwo(i, j + 1)

            return ways

        return _upwo(0, 0)

            