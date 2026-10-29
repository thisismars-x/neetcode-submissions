class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        table = {}
        def _dfs(amt: int) -> int:
            if amt in table: return table[amt]
            if amt == 0: return 0
            if amt < 0: return float("inf")
            table[amt] = min(1 + _dfs(amt - x) for x in coins)
            return table[amt]

        ans = _dfs(amount)
        return ans if ans != float("inf") else -1