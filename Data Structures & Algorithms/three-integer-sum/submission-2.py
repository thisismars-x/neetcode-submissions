class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        
        for i in range(len(nums) - 2):
            left, right, up = i, i + 1, len(nums) - 1
        
            required_sum = -nums[left]
            while right < up:
                if nums[right] + nums[up] == required_sum:
                    res.add(tuple(sorted([nums[left], nums[right], nums[up]])))
                    right += 1
                    up -= 1
                elif nums[right] + nums[up] < required_sum: right += 1
                else: up -= 1
        

        return list(list(x) for x in res)