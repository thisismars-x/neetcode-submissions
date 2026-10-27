class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        sub = []
        def _backtrack(i: int):
            if i >= len(nums):
                res.append(sub.copy())
                return

            sub.append(nums[i])
            _backtrack(i + 1)
            sub.pop()
            _backtrack(i + 1)

        _backtrack(0)
        return res