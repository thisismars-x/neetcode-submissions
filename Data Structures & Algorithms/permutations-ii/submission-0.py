class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = set()

        def _perms(curr: list[int], visited: set[int]):
            if len(curr) == len(nums):
                res.add(tuple(curr))
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
        return [list(x) for x in res]

            