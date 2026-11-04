class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        from functools import cache

        @cache
        def _dfs(i: int, mc: int) -> int:
            if i >= len(cost):
                return mc

            return min(
                _dfs(i + 1, mc + cost[i]),
                _dfs(i + 2, mc + cost[i])
            )

        return min(
            _dfs(0, 0),
            _dfs(1, 0)
        )