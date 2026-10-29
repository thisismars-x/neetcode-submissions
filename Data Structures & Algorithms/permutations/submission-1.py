class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        def _dfs(curr: list[int], used: set[int]):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in range(len(nums)):
                if i in used:
                    continue

                used.add(i)
                curr.append(nums[i])

                _dfs(curr, used)

                curr.pop()
                used.remove(i)

        _dfs([], set[int]())

        return res
        