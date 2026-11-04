class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # looks like a dp problem to me??
        from functools import cache

        @cache
        def _dfs(i: int) -> bool:
            if i >= len(nums) - 1:
                return True

            how_many_steps_can_you_take = nums[i]
            for j in range(1, how_many_steps_can_you_take + 1):
                if _dfs(j + i):
                    return True

            return False

        return _dfs(0)