class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque

        LAND = (1 << 31) - 1
        TREASURE = 0
        WATER = -1

        r, c = len(grid), len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        q = deque()

        # Start from every treasure
        for i in range(r):
            for j in range(c):
                if grid[i][j] == TREASURE:
                    q.append((i, j))

        while q:
            i, j = q.popleft()

            for dx, dy in dirs:
                ni, nj = i + dx, j + dy

                if (
                    0 <= ni < r
                    and 0 <= nj < c
                    and grid[ni][nj] == LAND
                ):
                    grid[ni][nj] = grid[i][j] + 1
                    q.append((ni, nj))