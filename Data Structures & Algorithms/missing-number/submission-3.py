class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for n in nums:
            if n == res: res += 1
            else: return res
        return res
