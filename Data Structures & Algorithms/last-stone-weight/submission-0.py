class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        import heapq
        heapq.heapify_max(stones)

        while len(stones) > 1:
            x, y = heapq.heappop_max(stones), heapq.heappop_max(stones)
            if x == y:
                continue
            if x > y:
                heapq.heappush_max(stones, x - y)

        return stones[0] if stones else 0