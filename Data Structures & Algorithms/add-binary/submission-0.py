class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = ''

        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            x = int(a[i]) if i >= 0 else 0
            y = int(b[j]) if j >= 0 else 0

            s = x ^ y ^ carry
            carry = (x & y) | (x & carry) | (y & carry)

            res = str(s) + res

            i -= 1
            j -= 1

        return res