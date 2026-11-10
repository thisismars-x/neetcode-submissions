class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])

        # count how many cells is surrounded by another cell
        
        visited = set()

        def _dfs(i: int, j: int) -> int:
            visited.add((i, j))

            ip = 4 # guess a cell is covered by water in all 4 sides initialyy
            for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                i2, j2 = i + di, j + dj

                if 0 <= i2 < r and 0 <= j2 < c and grid[i2][j2]:
                    if (i2, j2) not in visited:
                        ip -= 1
                        ip += _dfs(i2, j2)
                    else:
                        ip -= 1

            return ip

        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    return _dfs(i, j)