class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = [ [] for _ in range(n) ]
        for u,v,w in times:
            adj[u - 1].append((v, w))
        
        import heapq
        heap = [ (0, k) ]

        dist = [ float('inf') ] * n
        dist[k - 1] = 0

        while heap:
            _dist, node = heapq.heappop(heap)

            for children in adj[node - 1]:
                reach, w = children

                if _dist + w < dist[reach - 1]:
                    dist[reach - 1] = _dist + w
                    heapq.heappush(heap, (_dist + w, reach))

        res = max(dist)
        return res if res != float('inf') else -1