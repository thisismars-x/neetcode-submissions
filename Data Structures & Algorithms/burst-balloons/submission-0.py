class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        nums = [1] + nums + [1]

        from functools import cache

        @cache
        def _dfs(l: int, r: int) -> int:
            if l == r - 1:
                return 0

            best = 0
            for k in range(l + 1, r):
                burst = _dfs(l, k) + (nums[l] * nums[k] * nums[r]) + _dfs(k, r)
                best = max(best, burst)

            return best

        return _dfs(0, len(nums) - 1)