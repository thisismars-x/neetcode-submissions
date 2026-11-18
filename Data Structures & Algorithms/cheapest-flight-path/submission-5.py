class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = {i: [] for i in range(n)}
        for u,v,w in flights: adj[u].append((v, w))
        
        dist = [ float('inf') ] * n
        dist[src] = 0
        
        for _ in range(k + 1):
            tmp = dist.copy()

            for u in range(n):
                for v, w in adj[u]:
                    if dist[u] + w < tmp[v]:
                        tmp[v] = dist[u] + w
            dist = tmp
       
        return dist[dst] if dist[dst] != float('inf') else -1 