class Solution:
    def rob(self, nums: List[int]) -> int:
        
        from functools import cache

        @cache
        def _dfs(i: int, mc: int):
            if i >= len(nums):
                return mc

            return max(
                _dfs(i + 1, mc), # do not steal
                _dfs(i + 2, mc + nums[i])
            )

        return max(
            _dfs(0, 0),
            _dfs(1, 0)
        )