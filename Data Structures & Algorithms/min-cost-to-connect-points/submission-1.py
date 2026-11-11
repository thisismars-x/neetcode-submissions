class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        mst = 0

        used = [ False ] * n

        import heapq
        heap = [ (0, 0) ]
        count = 0

        while count < n:
            wt, u = heapq.heappop(heap)
            if used[u]:
                continue

            mst += wt
            used[u] = True
            count += 1

            for v in range(n):
                if used[v]:
                    continue

                d = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                heapq.heappush(heap, (d, v))

        return mst 