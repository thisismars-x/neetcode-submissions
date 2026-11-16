class Solution:
    def countBits(self, n: int) -> List[int]:
        # this can be done in O(nlogn) easily
        # but there must exist an even faster algo
        # return [i.bit_count() for i in range(n + 1)]

        def bit_count(x: int) -> int:
            # O(logn)
            res = 0
            while x:
                x &= (x - 1)
                res += 1
            return res

        return [bit_count(x) for x in range(n + 1)]

        