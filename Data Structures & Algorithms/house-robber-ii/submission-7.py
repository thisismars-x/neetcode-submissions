class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        # same like robber 1 if
        from functools import cache

        @cache
        def _r(i: int, arr: tuple[int]) -> int:
            if i >= len(arr):
                return 0
                
            return max(
                arr[i] + _r(i + 2, arr),
                _r(i + 1, arr)
            )

        arr1 = tuple(nums[:-1])
        arr2 = tuple(nums[1:])
        return max(_r(0, arr2), _r(0, arr1))
