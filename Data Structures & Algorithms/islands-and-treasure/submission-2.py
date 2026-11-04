class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque

        r, c = len(grid), len(grid[0])
        treasure = deque()
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    treasure.append((i, j))

        while treasure:
            n = len(treasure)
            
            for _ in range(n):
                i, j = treasure.popleft()

                for  di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    i2, j2 = di + i, dj + j
                    if 0 <= i2 < r and 0 <= j2 < c and grid[i2][j2] == (2**31) - 1:
                        grid[i2][j2] = grid[i][j] + 1
                        treasure.append((i2, j2))

            