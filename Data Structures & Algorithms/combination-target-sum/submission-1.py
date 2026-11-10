class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res_g = []

        def _cs(i: int, k: int, res: list[int]):
            if k == 0:
                res_g.append(res[:])
                return

            if k < 0:
                return

            if i > len(nums) - 1:
                return

            _cs(i, k - nums[i], res + [nums[i]])
            _cs(i + 1, k, res)

        _cs(0, target, [])
        return res_g

        