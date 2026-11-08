class Solution:
    def numSquares(self, n: int) -> int:
        from math import isqrt

        squares = [i * i for i in range(1, isqrt(n) + 1)]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for s in range(1, n + 1):
            dp[s] = min(dp[s - square] for square in squares if square <= s) + 1

        return dp[n]