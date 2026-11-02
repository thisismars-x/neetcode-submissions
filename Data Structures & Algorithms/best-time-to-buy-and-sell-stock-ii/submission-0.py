class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        from functools import cache

        @cache
        def _dfs(i: int, buy: bool) -> int:

            if i >= len(prices):
                return 0

            if buy:
                v = max(
                    _dfs(i + 1, not buy) - prices[i],
                    _dfs(i + 1, buy)
                )
            else:
                v = max(
                    _dfs(i + 1, not buy) + prices[i],
                    _dfs(i + 1, buy)
                )

            return v

        return _dfs(0, True)
