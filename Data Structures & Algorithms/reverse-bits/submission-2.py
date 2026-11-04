class Solution:
    def reverseBits(self, n: int) -> int:
        
        res = 0x0000
        # repeatedly take the last bit and do your thing
        for i in range(32):
            leftmost = (n >> i) & 1
            res |= (leftmost << (32 - i - 1))
        return res