class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        from functools import cache

        @cache
        def _dfs(k: int):
            if k == 0:
                return 0
            if k < 0:
                return float('inf')

            return min(
                1 + _dfs(k - c) for c in coins
            ) 


        res = _dfs(amount)
        return res if res != float('inf') else -1