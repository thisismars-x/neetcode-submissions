# Rotting fruit:
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        
        rotten, fresh = deque(), set()
        r, c = len(grid), len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2: rotten.append((i, j))
                elif grid[i][j] == 1: fresh.add((i, j))
                
        if not fresh: return 0
        if not rotten: return -1

        n_minutes = 0
        
        while rotten:
            l = len(rotten)
            
            before_rotting = len(fresh)
            
            for _ in range(l):
                i, j = rotten.popleft()
                for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                    i2, j2 = i + di, j + dj
                    if 0 <= i2 < r and 0 <= j2 < c and (i2, j2) in fresh:
                        fresh.remove((i2, j2))
                        rotten.append((i2, j2))
            
            after_rotting = len(fresh)

            n_minutes += 1
            
            if after_rotting == 0: return n_minutes
            if after_rotting == before_rotting: return -1
        
        return n_minutes