class Solution:
    def countBits(self, n: int) -> List[int]:
        # this can be done in O(nlogn) easily
        # but there must exist an even faster algo

        return [i.bit_count() for i in range(n + 1)]
        