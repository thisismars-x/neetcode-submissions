class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            number = str(x)[1:][::-1]
        else:
            number = str(x)[::-1]
        
        res = int(number) * (-1 if x < 0 else 1)
        if res > (1 << 31) - 1 or res < -(1 << 31): return 0
        return res