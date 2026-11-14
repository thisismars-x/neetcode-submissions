class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        max_, min_, cmax, cmin = nums[0], nums[0], 0, 0
        total = 0

        for num in nums:
            cmax = max(cmax + num, num)
            cmin = min(cmin + num, num)
            total += num
            max_ = max(max_, cmax)
            min_ = min(min_, cmin)

        return max(max_, total - min_) if max_ > 0 else max_