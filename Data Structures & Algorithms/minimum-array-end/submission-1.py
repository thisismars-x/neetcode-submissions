class Solution:
    def minEnd(self, n: int, x: int) -> int:
        _x, _n = [0] * 64, [0] * 64
        n -= 1

        for i in range(32):
            _x[i] = (x >> i) & 1
            _n[i] = (n >> i) & 1

        inx, inn = 0, 0
        while inx < 63:
            while inx < 63 and _x[inx] != 0:
                inx += 1
            
            _x[inx] = _n[inn]
            inx += 1
            inn += 1

        res = 0
        for i in range(64):
            if _x[i]:
                res += (1 << i)

        return res
