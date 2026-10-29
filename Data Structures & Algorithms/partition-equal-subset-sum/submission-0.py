class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # the question can be reframed as can sum(arr) / 2 
        # be reached using arr
        s = sum(nums)
        if s & 1: return False
        s >>= 1

        from functools import cache

        @cache
        def _dfs(i: int, k: int) -> bool:
            if i == len(nums) and k != 0:
                return False

            if nums[i] == k:
                return True

            return _dfs(i + 1, k - nums[i]) or _dfs(i + 1, k)

        return _dfs(0, s)

            