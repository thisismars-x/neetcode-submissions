class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # so do djikstra to get shortest distances and then take the max of shortest dist
        dist = [ float('inf') ] * (n + 1) # do not touch dist[0]
        dist[k] = 0

        from collections import defaultdict
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        import heapq
        pq = [(0, k)]

        while pq:
            ds, node = heapq.heappop(pq)

            for reach_node in adj[node]:
                v, w = reach_node
                
                if ds + w < dist[v]:
                    dist[v] = ds + w
                    heapq.heappush(pq, (dist[v], v))


        v = max(dist[1:])
        return v if v != float('inf') else -1