class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from functools import reduce
        from operator import xor
        return reduce(xor, nums)