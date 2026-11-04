class Solution:
    def rob(self, nums: List[int]) -> int:

        from functools import cache
        @cache
        def _dfs(i: int, first: bool) -> int:
            if i >= len(nums):
                return 0

            skip = _dfs(i + 1, first)

            take = 0
            if not (i == len(nums) - 1 and first):
                take += nums[i] + _dfs(i + 2, first or i == 0)

            return max(skip, take)

        return _dfs(0, False)