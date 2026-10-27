class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        # this looks like a bfs problem
        LAND = (1 << 31) - 1
        TREASURE = 0
        WATER = -1

        r, c = len(grid), len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        from collections import deque
        q = deque()
        for i in range(r):
            for j in range(c):
                if grid[i][j] == TREASURE:
                    q.append((i, j))

        while q:
            i, j = q.popleft()
            for dx, dy in dirs:
                _i, _j = i + dx, j + dy
                if 0 <= _i < r and 0 <= _j < c and grid[_i][_j] == LAND:
                    grid[_i][_j] = grid[i][j] + 1
                    q.append((_i, _j))




