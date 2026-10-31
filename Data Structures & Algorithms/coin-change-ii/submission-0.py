class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        from functools import cache

        @cache
        def _dfs(i: int, k: int) -> int:
            if k == 0:
                return 1
            if i == len(coins):
                return 0
            if k < 0:
                return 0

            return _dfs(i, k - coins[i]) + _dfs(i + 1, k)

        return _dfs(0, amount)