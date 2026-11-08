class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        from functools import cache

        @cache
        def _cs(s: int) -> int:
            if s == 0:
                return 1

            if s < 0:
                return 0 

            return sum(_cs(s - n) for n in nums)

        return _cs(target)

            

