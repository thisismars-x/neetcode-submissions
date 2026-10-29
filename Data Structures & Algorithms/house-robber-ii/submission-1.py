class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # this is very similar to the robberI problem

        n = len(nums)
        if n == 1: return nums[0]

        c = {}

        def _dfs(i: int, first: bool) -> int:
            if (i, first) in c: return c[(i, first)]
            if i >= n:
                return 0

            skip = _dfs(i + 1, first)

            # last house can not be robbed if first was robbed
            take = 0
            if not (i == n - 1 and first):
                take += nums[i] + _dfs(i + 2, first or i == 0) # if we are at 0th house first beceomes True

            c[(i, first)] = max(skip, take)
            return c[(i, first)]

        return _dfs(0, False)