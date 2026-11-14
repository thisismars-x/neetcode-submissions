class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        count = {
            5: 0,
            10: 0,
            20: 0
        }
        
        def _can_make_change(n: int):
            for k in (10, 5):
                while count[k] > 0 and n >= k:
                    n -= k
                    count[k] -= 1

            return n == 0

        for c in bills:
            if not _can_make_change(c - 5):
                return False
            count[c] += 1

        return True