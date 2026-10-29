class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        table = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    table[i] = max(table[i], table[j] + 1)

        return max(table)
