class Solution:
    def stoneGameII(self, piles: List[int]) -> int:


        from functools import cache
        @cache
        def _dfs(alice: bool, i: int, M: int) -> int:
            if i == len(piles):
                return 0

            res = 0 if alice else float('inf')
            total = 0

            for X in range(1, 2*M + 1):
                if i + X > len(piles):
                    break
                    
                if alice:
                    total += piles[i + X - 1]
                    res = max(res, total + _dfs(False, i + X, max(M, X)))
                else:
                    res = min(res, _dfs(True, i + X, max(M, X)))

            return res

        return _dfs(True, 0, 1)