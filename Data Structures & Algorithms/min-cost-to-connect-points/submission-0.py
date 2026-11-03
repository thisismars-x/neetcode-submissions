class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # this must be a minimum spanning tree problem?
        # using prims algorithm
        n = len(points)
        dist = [ float('inf') ] * n
        dist[0] = 0
        used = [ False ] * n
        total = 0

        for _ in range(n):
            u = min(
                (i for i in range(n) if not used[i]),
                key = lambda i: dist[i]
            )

            used[u] = True
            total += dist[u]
            for v in range(n):
                if not used[v]:
                    d = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    if d < dist[v]:
                        dist[v] = d

                   

        return total