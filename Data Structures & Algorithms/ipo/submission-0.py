class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        min_cap = list(zip(capital, profits))
        
        import heapq

        heapq.heapify(min_cap)

        max_prof = []

        while k:
            while min_cap and min_cap[0][0] <= w:
                c, p = heapq.heappop(min_cap)
                heapq.heappush(max_prof, -p)

            if not max_prof: break

            w += -1 * heapq.heappop(max_prof)

            k -= 1

        return w