class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        tsum = sum(stones)
        from functools import cache
        
        @cache
        def _dfs(i: int, t: int):
            if t >= (tsum + 1) // 2 or i == len(stones):
                return abs(t - (tsum - t))

            return min(
                _dfs(i + 1, t + stones[i]),
                _dfs(i + 1, t)
            )

        return _dfs(0, 0)
