class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def _dfs(i: int, k: int, curr: list[int]):

            if k == 0:
                res.append(curr.copy())
                return

            if i >= n or k < 0:
                return
            
            curr.append(nums[i])
            _dfs(i, k - nums[i], curr)
            curr.pop()

            _dfs(i + 1, k, curr)

        _dfs(0, target, [])
        return res