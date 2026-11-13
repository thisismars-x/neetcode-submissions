class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        from sys import maxsize
        
        min_len = maxsize
        start = end = 0

        curr_sum = 0
        while end < len(nums):
            curr_sum += nums[end]

            while curr_sum >= target:
                min_len = min(min_len, end - start + 1)
                curr_sum -= nums[start]
                start += 1

            end += 1

        return min_len % maxsize