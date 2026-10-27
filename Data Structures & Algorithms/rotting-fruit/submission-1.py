class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        r, c = len(grid), len(grid[0])

        # looks like a bfs problem
        from collections import deque
        rotten = deque()
        non_rotten = deque()

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    non_rotten.append((i, j))

        if len(non_rotten) == 0: return 0

        # if in any round non_rotten does not decrease with rotting that means
        # there is no valid solution

        dirs = ((0,1),(1,0),(-1,0),(0,-1))

        count = 0

        while True:
            before_round = len(non_rotten)
            lr = len(rotten)
            for _ in range(lr):
                x, y = rotten.popleft() # add it back later
                for dx, dy in dirs:
                    xx, yy = x + dx, y + dy
                    if 0 <= xx < r and 0 <= yy < c and (xx, yy) in non_rotten:
                        non_rotten.remove((xx, yy))
                        rotten.append((xx, yy))
                rotten.append((x, y))
            after_round = len(non_rotten)

            count += 1
            
            if after_round == 0: # result found
                return count
            if after_round == before_round:
                return -1

        return count
    