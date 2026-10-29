class Solution:
    def rob(self, nums: List[int]) -> int:

        # been doing neetcode for too long
        # after this question i will do something else
        n = len(nums)
        max_ = 0

        c = {}

        def _dfs(i: int, curr: int):
            if (i, curr) in c:
                return c[(i, curr)]

            if i >= n:
                return curr
            
            res = max(
                _dfs(i + 2, curr + nums[i]),
                _dfs(i + 1, curr)
            )
            c[(i, curr)] = res
            return res

        return _dfs(0, 0)