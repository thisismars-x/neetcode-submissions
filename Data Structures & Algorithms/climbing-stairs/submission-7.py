class Solution:
    def climbStairs(self, n: int) -> int:
        
        from functools import cache

        @cache
        def _cs(i: int):
            if i == n:
                return 1
            if i > n:
                return 0

            return _cs(i + 1) + _cs(i + 2)
        
        return _cs(0)