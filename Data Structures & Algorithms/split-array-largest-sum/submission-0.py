class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        from functools import cache

        @cache
        def _dfs(i: int, t: int):
            if i == len(nums):
                return 0 if t == 0 else float('inf')
            if t == 0:
                return float('inf')

            res = float('inf')
            curr_sum = 0
            for j in range(i, len(nums) - t + 1):
                curr_sum += nums[j]
                res = min(res, max(curr_sum, _dfs(j + 1, t - 1)))
            return res

        return _dfs(0, k)