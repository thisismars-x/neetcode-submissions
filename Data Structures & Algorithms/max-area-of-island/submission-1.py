class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        visited = set()

        def _dfs(i: int, j: int):
            if (i, j) in visited:
                return

            visited.add((i, j))

            for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                i2, j2 = i + di, j + dj
                if 0 <= i2 < r and 0 <= j2 < c and grid[i2][j2] == 1:
                    if (i2, j2) not in visited:
                        _dfs(i2, j2)
        

        max_area = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = len(visited)
                    _dfs(i, j)
                    max_area = max(max_area, len(visited) - area)

        return max_area