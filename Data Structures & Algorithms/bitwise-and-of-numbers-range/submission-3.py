class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i = 0
        while left != right:
            left, right = left >> 1, right >> 1
            i += 1
        return left << i

        # This is TLE
        # from functools import reduce
        # from operator import and_
        # return reduce(and_, range(left, right + 1))