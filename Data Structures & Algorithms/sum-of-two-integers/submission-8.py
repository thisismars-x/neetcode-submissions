class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        c = 0

        for i in range(32):
            lo_a, lo_b = (a >> i) & 1, (b >> i) & 1
            value = lo_a ^ lo_b ^ carry
            carry = (lo_a & lo_b) | (lo_a & carry) | (lo_b & carry)
            c |= (value << i)

        if c > 0x7fffffff:
            c = ~(c ^ 0xffffffff)

        return c


