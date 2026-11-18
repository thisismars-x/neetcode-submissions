class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = {1 + i: [] for i in range(n)}
        for u, v, w in times:
            adj[u].append((v, w))
        
        dist = [ float('inf') ] * (n + 1)
        dist[k] = 0
        
        import heapq
        heap = [ (0, k) ]
        
        while heap:
            ds, node = heapq.heappop(heap)
            
            for child, w in adj[node]:
                new_ds = ds + w
                if new_ds < dist[child]:
                    dist[child] = new_ds
                    heapq.heappush(heap, (new_ds, child))
                    
        return max(dist[1:]) if max(dist[1:]) != float('inf') else -1
                    