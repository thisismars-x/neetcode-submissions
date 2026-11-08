class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        from functools import cache

        @cache
        def _dfs(i: int):
            if i > len(stoneValue) - 1:
                return 0

            res = -float('inf')
            total = 0

            for j in range(i, min(i + 3, len(stoneValue))):
                total += stoneValue[j]
                res = max(
                    res, total - _dfs(j + 1)
                )

            return res

        res = _dfs(0)
        if res == 0:
            return 'Tie'

        if res > 0:
            return 'Alice'

        return 'Bob'
            
