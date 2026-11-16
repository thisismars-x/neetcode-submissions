class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        if len(a) < len(b):
            a, b = b, a

        n1, n2 = len(a), len(b)
        i = 1
        carry = 0

        res = []

        while i <= n2:
            la, lb = int(a[n1 - i]), int(b[n2 - i])
            csum = carry ^ la ^ lb
            carry = carry & la | carry & lb | la & lb
            res.append(str(csum))
            i += 1

        while i <= n1:
            la = int(a[n1 - i])
            csum = la ^ carry
            carry = carry & la
            res.append(str(csum))
            i += 1

        if carry:
            res.append(str(carry))


        return ''.join(res[::-1])
