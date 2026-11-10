class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        r, c = len(heights), len(heights[0])

        import heapq

        # variant on djisktra
        dist = [ float('inf') for _ in range(r * c) ]
        dist[0] = 0

        heap = [ (0, (0, 0)) ]

        while heap:
            distance, (i, j) = heapq.heappop(heap)

            for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                i2, j2 = i + di, j + dj

                if 0 <= i2 < r and 0 <= j2 < c:
                    add_dist = abs(heights[i2][j2] - heights[i][j])
                    new_dist = max(add_dist, distance)
                    if new_dist < dist[(i2 * c) + j2]:
                        dist[(i2 * c) + j2] = new_dist
                        heapq.heappush( heap, (new_dist, (i2, j2)) )

        return dist[-1]