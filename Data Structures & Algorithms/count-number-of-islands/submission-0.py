class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # trying it for the sake of it

        visited = set()
        
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1), (0, 0)]

        r, c = len(grid), len(grid[0])

        def _dfs(x: int, y: int):
            visited.add((x, y))
            for (dx, dy) in dirs:
                _x, _y = x + dx, y + dy
                if 0 <= _x < r and 0 <= _y < c and grid[x][y] == "1" and (_x, _y) not in visited:
                    _dfs(_x, _y)

                

        cunt = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1" and (i, j) not in visited:
                    cunt += 1
                    _dfs(i, j)

        return cunt