class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r, c = len(grid), len(grid[0])

        visited = set()
        
        def _dfs(i: int, j: int):
            if (i, j) in visited:
                return

            visited.add((i, j))
            for di, dj in ( (0, 1), (0, -1), (1, 0), (-1, 0) ):
                i2, j2 = i + di, j + dj
                if 0 <= i2 < r and 0 <= j2 < c and grid[i2][j2] == '1':
                    _dfs(i2, j2)

        ti = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1' and (i, j) not in visited:
                    _dfs(i, j)
                    ti += 1

        return ti