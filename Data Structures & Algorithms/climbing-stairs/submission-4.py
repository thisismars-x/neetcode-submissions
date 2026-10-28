class Solution:
    def climbStairs(self, n: int) -> int:

        cache = {}
        # let me write the recursive version first
        def _cs(rem: int) -> int:
            if rem in cache: return cache[rem]
            if rem == 0: return 1
            if rem < 0: return 0

            c = _cs(rem - 1) + _cs(rem - 2)
            cache[rem] = c
            return c

        return _cs(n)