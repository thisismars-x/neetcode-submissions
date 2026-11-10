class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        def _perms(curr: list[int], visited: set[int]):
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for i in range(len(nums)):
                if i in visited:
                    continue

                visited.add(i)
                curr.append(nums[i])
                _perms(curr, visited)

                visited.remove(i)
                curr.pop()

        _perms([], set())
        return res