class Solution:
    def hammingWeight(self, n: int) -> int:
        # number of 1 bits

        tc = 0
        while n:
            tc += 1
            n &= (n - 1)

        return tc

        