class Solution:
    def reverseBits(self, n: int) -> int:
        # the naive way
        # n = bin(n)[::-1][:-2]
        # nn = len(n)
        # n = n + ("0"*(32 - nn))
        # return int('0b' + n, 2)
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res |= bit << (31 - i)

        return res