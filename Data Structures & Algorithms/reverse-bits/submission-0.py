class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)[::-1][:-2]
        nn = len(n)
        n = n + ("0"*(32 - nn))
        return int('0b' + n, 2)