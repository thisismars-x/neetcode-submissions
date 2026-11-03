class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # use bellman ford but relax edges only a total of k times?
        prices = [ float('inf') ] * n
        prices[src] = 0
           
        for _ in range(k + 1):
            tmp = prices.copy()
            for u, v, w in flights:
                if prices[u] != float('inf') and prices[u] + w < tmp[v]:
                    tmp[v] = prices[u] + w
            prices = tmp

        return prices[dst] if prices[dst] != float('inf') else -1