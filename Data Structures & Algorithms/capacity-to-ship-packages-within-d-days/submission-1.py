class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def _can_ship(c: int) -> bool:
            nships, curr_c = 1, c

            for wt in weights:
                if curr_c - wt < 0:
                    nships += 1
                    if nships > days:
                        return False
                    curr_c = c

                curr_c -= wt

            return True

        lo, hi = max(weights), sum(weights)
        res = hi

        while lo <= hi:
            mid = (lo + hi) // 2
            if _can_ship(mid):
                res = min(res, mid)
                hi = mid - 1
            else:
                lo = mid + 1
        return res