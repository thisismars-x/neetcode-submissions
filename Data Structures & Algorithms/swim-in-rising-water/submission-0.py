class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        # djisktra variant
        import heapq
        pq = [ (grid[0][0], 0, 0) ] # total cost so far, r, c
        visited = {(0, 0)}

        n = len(grid)

        while pq:
            t, r, c = heapq.heappop(pq)
            if (r, c) == (n - 1, n - 1):
                return t

            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                r2, c2 = r + dr, c + dc

                if (
                    0 <= r2 < n and 0 <= c2 < n and
                    (r2, c2) not in visited
                ):
                    visited.add((r2, c2))
                    heapq.heappush(pq, ( max(t, grid[r2][c2]), r2, c2 ))