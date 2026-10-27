class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        from math import ceil

        # brute force solution
        n = len(piles)

        lo, hi = 1, max(piles)

        while lo <= hi:
            mid = (lo + hi) // 2

            time_for_mid = sum(( (int(ceil(x / mid))) for x in piles ))
            if time_for_mid > h: lo = mid + 1
            else: hi = mid - 1

        return lo