class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        c = {}

        
        def _dfs(i: int, b: bool) -> int:
            if i >= len(prices):
                return 0
            if (i, b) in c:
                return c[(i, b)]

            # ith day is cooldown day/ skip day
            pcool = _dfs(i + 1, b)
            if b:
                pb = _dfs(i + 1, False) - prices[i]
                pb = max(pb, pcool) 
                c[(i, b)] = pb
                return pb
            else:
                ps = _dfs(i + 2, True) + prices[i]
                ps = max(ps, pcool)
                c[(i, b)] = ps
                return ps

        return _dfs(0, True)