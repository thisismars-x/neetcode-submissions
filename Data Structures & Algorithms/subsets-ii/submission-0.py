class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        ans = set()

        def _swd(i: int, sub: list[int]):
            if i == len(nums):
                ans.add(tuple(sub))
                return

            sub.append(nums[i])
            _swd(i + 1, sub)
            sub.pop()
            _swd(i + 1, sub)

        nums.sort()
        _swd(0, [])
        return list((list(s) for s in ans))