class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = carry = 0
        for i in range(32):
            la, lb = (a >> i) & 1, (b >> i) & 1
            csum = la ^ lb ^ carry
            carry = la & lb | la & carry  | lb & carry
            res |= (csum << i)
        if res >= 0x8FFFFFFF: res = ~(res ^ 0xFFFFFFFF)
        return res