class Solution:
    def jump(self, nums: List[int]) -> int:
        
        # this is also dp isnt it
        from functools import cache

        @cache
        def _dfs(i: int) -> int:
            if i >= len(nums) - 1:
                return 0 # there is always a valid solution we will reach here

            n_steps = nums[i]
            ms = float('inf')
            for j in range(1, n_steps + 1):
                s = _dfs(i + j)
                ms = min(s, ms)

            return ms + 1

        return _dfs(0)