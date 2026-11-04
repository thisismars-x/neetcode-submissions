class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        from operator import xor
        from functools import reduce
        return reduce(xor, nums)