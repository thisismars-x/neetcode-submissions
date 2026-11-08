class Solution:
    def integerBreak(self, n: int) -> int:
        

        from functools import cache

        @cache
        def _dfS(m: int):
            if m == 1:
                return 1

            res = 0 if n == m else m
            for i in range(1, m):
                v = _dfS(i) * _dfS(m - i)
                res = max(res, v)

            return res

        return _dfS(n)