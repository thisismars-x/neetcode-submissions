class Solution:
    def isHappy(self, n: int) -> bool:
        
        def _gs(x: int) -> int:
            r = 0
            while x:
                low = x % 10
                r += (low * low)
                x //= 10
            return r

        visited = set()

            
        while n != 1:
            visited.add(n)
            n = _gs(n)
            if n in visited:
                return False

        return True