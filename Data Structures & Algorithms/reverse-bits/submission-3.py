class Solution:
    def reverseBits(self, n: int) -> int:

        res = 0
        
        for i in range(32):
            lb = ( (n >> i) & 1 )
            res |= ( lb << (31 - i) )

        return res