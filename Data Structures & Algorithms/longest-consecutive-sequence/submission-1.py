class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == 0: return 0

        from sys import maxsize
        max_len = -maxsize

        count = {}
        for number in nums:
            count[number] = count.get(number - 1, 0) + 1 

        return max(count.values())
        