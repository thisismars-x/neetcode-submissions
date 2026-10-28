class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        c = {}
            
        def _dfs(n: int):
            if n in c: return c[n]
            if n >= len(cost): return 0

            c[n] = cost[n] + min(_dfs(n + 1), _dfs(n + 2))
            return c[n]

        return min(_dfs(0), _dfs(1))