class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        table = {}
        def _dfs(i: int, cs: int) -> int:
            if i == len(nums):
                if cs == target:
                    return 1
                return 0

            if (i, cs) in table:
                return table[(i, cs)]

            table[(i, cs)] = _dfs(i + 1, cs + nums[i]) + _dfs(i + 1, cs - nums[i])
            return table[(i, cs)]

        return _dfs(0, 0)
