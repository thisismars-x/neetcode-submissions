class Solution:
    def climbStairs(self, n: int) -> int:

        from functools import cache

        @cache
        def _cs(nx: int):
            if nx == 0: return 1
            if nx < 0: return 0
            return (_cs(nx - 2)) + (_cs(nx - 1))

        return _cs(n)