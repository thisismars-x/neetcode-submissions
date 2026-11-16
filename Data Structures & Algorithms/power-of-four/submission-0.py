class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        from math import log

        for i in range(int(log(n, 4)) + 1):
            if 4 ** i == n:
                return True

        return False