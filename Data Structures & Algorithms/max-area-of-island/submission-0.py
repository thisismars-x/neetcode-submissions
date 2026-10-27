class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_len = 0
        r, c = len(grid), len(grid[0])

        visited = set()

        dirs = ((1, 0), (0, 1), (0, -1), (-1, 0))

        def _dfs(i: int, j: int):
            if (i, j) in visited: return 
            visited.add((i, j))

            for di, dj in dirs:
                _i, _j = i + di, j + dj
                if 0 <= _i < r and 0 <= _j < c and grid[_i][_j] == 1:
                    _dfs(_i, _j)

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1 and (i, j) not in visited:
                    prev_len = len(visited)
                    _dfs(i, j)
                    max_len = max(max_len, len(visited) - prev_len)

        return max_len
        