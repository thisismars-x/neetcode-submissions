class Solution:
    def getSum(self, a: int, b: int) -> int:

        # the premise is integers are 32 bit fixed
        mask = 0xffffffff
        carry = 0

        res = 0
        for i in range(32):
            bit_a, bit_b = (a >> i) & 1, (b >> i) & 1
            s = bit_a ^ bit_b ^ carry
            carry = (bit_a & bit_b) | (bit_a & carry) | (bit_b & carry)
            res |= (s << i)

        if res > 0x7fffffff:
            res = ~(res ^ mask)

        return res
