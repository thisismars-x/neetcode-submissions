class Solution:
    def rob(self, nums: List[int]) -> int:
        from functools import cache

        @cache
        def _r(i: int) -> int:
            if i >= len(nums):
                return 0
                
            return max(
                nums[i] + _r(i + 2),
                _r(i + 1)
            )

        return _r(0)