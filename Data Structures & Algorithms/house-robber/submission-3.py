class Solution:
    def rob(self, nums: List[int]) -> int:

        # been doing neetcode for too long
        # after this question i will do something else
        n = len(nums)
        max_ = 0

        c = {}

        def _dfs(i: int) -> int:
            if i in c: return c[i]
            if i >= n:
                return 0

            res = max(nums[i] + _dfs(i + 2), _dfs(i + 1))
            c[i] = res
            return res

        return _dfs(0)