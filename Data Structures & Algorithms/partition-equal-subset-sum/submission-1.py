class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        s = sum(nums)
        if s & 1:
            return False
        ass = s >> 1

        def _dfs(i: int, k: int) -> bool:
            if k == 0:
                return True

            if k < 0 or i > len(nums) - 1:
                return False

            return _dfs(i + 1, k - nums[i]) or _dfs(i + 1, k)

        return _dfs(0, ass)