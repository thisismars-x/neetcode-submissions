class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:

        from functools import cache

        @cache
        def _mccs(i: int):
            if i == len(cost):
                return 0
            if i > len(cost):
                return float('inf')

            return min(_mccs(i + 1), _mccs(i + 2)) + cost[i]

        return min(_mccs(0), _mccs(1))